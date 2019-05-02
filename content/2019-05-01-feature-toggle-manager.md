---
Title: Usando Toggles com Togglz e Spring Boot
Date: 2019-05-01 18:00
Category: development
tags: feature-toggle, togglz, spring-boot
Slug: feature-toggle-manager
Summary: Passo a passo de como criar uma biblioteca de feature-toggle com Togglz e Spring Boot.
---

## 1.Introdução

Nossa aplicação está crescendo, queremos ter um controle maior do envio de novas funcionalidades para produção, fazer um roolback rápido de uma funcionalidade caso não esteja funcionando de acordo, realizar testes A/B de novas funcionalidades, realizar testes em produção de forma controlada e segura, habilitar fluxos distintos caso uma funcionalidade X seja utilizada pelo cliente Y ou Z. E queremos fazer tudo isso de forma simples, segura e controlada. A pergunta então é como?

Existe um design pattern que muitos já conhecem que é [Feature Toggle](https://www.martinfowler.com/articles/feature-toggles.html), que entre outras coisas, permite determinar em tempo de execução se uma determinada funcionalidade está habilitada ou não.

Recentemente em meu time, estamos ocupando cada vez mais o uso de Fature Toggles, com o objetivo de enviar códigos para produção de forma mais segura, possibilitando o roolback mais rápido, ou então realizar testes em produção de forma mais controlada, como por exemplo, habilitar uma nova funcionalidade apenas para um determinado IP, ou permitir o uso da nova funcionalidade apenas para 5% dos usuários.

A forma que fazemos isso é:
```java
if (MY_FEATURE.isActive()) {
    // código da funcionalidade aqui
}
```

Não sei você, mas o fato de ter **IFs** espalhados em todo o código me incomoda, pois o torna um pouco sujo espalhando as tomadas de decisões de novos fluxos por setores que não deveriam ser responsáveis por isso. Além de adicionar complexidade para casos que é uma feature temporária e se deseja remover o código não mais utilizado.

Então, como resolvemos isso? Como conseguimos eliminar os IFs por todo o código e isolar as novas funcionalidades?

Para isso vamos utilizar o framework [Togglz](https://www.togglz.org/) que provê uma implementação para o design pattern Feature Toggle e é simples de usar e customizar, juntamente com Spring Boot.

### 2.Maven dependências

Iniciando, vamos adicionar as dependências do *Spring Boot* e *Togglz*:

```xml
<dependencies>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-aop</artifactId>
            <version>5.0.1.RELEASE</version>
            <scope>compile</scope>
        </dependency>
        <dependency>
            <groupId>org.aspectj</groupId>
            <artifactId>aspectjweaver</artifactId>
            <version>1.8.12</version>
            <scope>compile</scope>
        </dependency>
        <dependency>
            <groupId>org.togglz</groupId>
            <artifactId>togglz-spring-boot-starter</artifactId>
            <version>2.6.1.Final</version>
        </dependency>
        <dependency>
            <groupId>org.togglz</groupId>
            <artifactId>togglz-spring-security</artifactId>
            <version>2.6.1.Final</version>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
        </dependency>
        <dependency>
            <groupId>com.h2database</groupId>
            <artifactId>h2</artifactId>
            <version>1.4.194</version>
        </dependency>
    </dependencies>
```

## 3.Togglz Configuração

Após adicionar as dependências criamos um enumeration que implementa a interface *Feature* e contém a lista de novas features.

```java
public enum MyFeatures implements Feature {

    @Label("Employee Management Feature")
    @EnabledByDefault
    @DefaultActivationStrategy(id = SystemPropertyActivationStrategy.ID,
            parameters = {
                    @ActivationParameter(
                            name = SystemPropertyActivationStrategy.PARAM_PROPERTY_NAME,
                            value = "employee.feature"),
                    @ActivationParameter(
                            name = SystemPropertyActivationStrategy.PARAM_PROPERTY_VALUE,
                            value = "true") })
    EMPLOYEE_MANAGEMENT_FEATURE;

    public boolean isActive() {
        return FeatureContext.getFeatureManager().isActive(this);
    }
}
```

O enum *MyFeature* define um método chamado *isActive()* que verifica quando a feature está habilitada ou não. Este comportamenteo é controlado por uma flag (*@EnabledByDefault*) e opcionalmente uma estratégia de ativação.

A biblioteca *Togglz* prover uma variedade de estratégias de ativação que podem ser usadas para determinar se uma feature está habilitada baseada em uma certa condição.

No casso da feature *EMPLOYEE_MANAGEMENT_FEATURE*, usamos *SystemPropertyActivationStrategy*, o qual avalia o estado da feature baseado no *System.property* do Java. O nome da propriedade de sistema são fornecidos através da anotação *ActivationParameter*.

O *Togglz* possui outras estratégias de ativação, tais como:

* **Username** - que permite uma feature seja ativa por uma lista de usuários específicos.
* **Userrole** - utiliza a role do usuário para determina o estado da feature.
* **Release Date** - automaticamente ativa a feature em uma certa data e tempo.
* **Gradual Rollot** - habilita uma feature para uma porcentagem de usuários.
* **ScriptEngine** - permite utilizar um script customizado em uma linguagem suportada para determinar se a feature está ativa ou não.
* **Server IP** - uma feature é habilitada baseada no endereço IP.
* **Custom Strategy** - permite adicionar uma estratégia customizada para habilitar ou não uma feature, como por exemplo baseada em feriados.

A biblioteca *togglz-spring-boot-starter* possui auto-configuração necessária para prover o bean *FeatureContext*. O único bean que precisamos definir é o *featureProvider*

```java
@Configuration
@EnableJpaRepositories("com.core.toggle")
@EntityScan("com.core.toggle")
public class ToggleConfiguration {

    @Bean
    public FeatureProvider featureProvider() {
        return new EnumBasedFeatureProvider(MyFeatures.class);
    }
}
```

## 4.Criando o Aspect

O próximo passo será criar um Aspect que intercepta o uso da anotação FeatureToggle e verifica se a feature fornecida no parâmetro está ativa ou não.

```java
@Aspect
@Configuration
public class FeaturesAspect {

    private Logger logger = LoggerFactory.getLogger(this.getClass());
    @Around(
            "@within(featureAssociation) || @annotation(featureAssociation)"
    )
    public Object around(ProceedingJoinPoint joinPoint, FeatureAssociation featureAssociation) throws Throwable {
        if (featureAssociation.value().isActive()) {
            return joinPoint.proceed();
        } else {
            logger.info("Feature " + featureAssociation.value().name() + " is not enabled!");
            return null;
        }
    }
}
```

Resta-nos definir uma anotação chamada **FeatureToggle** que terá um parâmetro *value()* do tipo *MyFeature*.

```java
@Target({ ElementType.METHOD, ElementType.TYPE })
@Retention(RetentionPolicy.RUNTIME)
public @interface FeatureToggle {
    MyFeatures value();
}
```

## 5.Testando

Para testar o uso da nossa estrutura de toggle vamos criar um simples exemplo que contenha uma feature para gerenciar o salário dos empregados de uma organização.

```java
@Entity
public class Employee {
 
    @Id
    private long id;
    private double salary;
     
    // standard constructor, getters, setters
}
```

```java
public interface EmployeeRepository
  extends CrudRepository<Employee, Long>{ }
```

Agora, vamos adicionar um serviço que irá aumentar o salário do empregado se a feature estiver ativa, adicionando a anotação *@FeatureToggle* ao método com o parâmetro **EMPLOYEE_MANAGEMENT_FEATURE**.

```java
@Service
public class SalaryService {

    @Autowired
    EmployeeRepository employeeRepository;

    @FeatureToggle(value = MyFeatures.EMPLOYEE_MANAGEMENT_FEATURE)
    public void increaseSalary(long id) {
        Employee employee = employeeRepository.findById(id).orElse(null);
        employee.setSalary(employee.getSalary() +
                employee.getSalary() * 0.1);
        employeeRepository.save(employee);
    }
}
```

Iremos criar o endpoint **/increaseSalary** para a chamada.

```java
@Controller
public class SalaryController {

    @Autowired
    SalaryService salaryService;

    @PostMapping("/increaseSalary")
    @ResponseBody
    public void increaseSalary(@RequestParam long id) {
        salaryService.increaseSalary(id);
    }
}
```

Por último, vamos adicionar um teste o qual chamaremos nossa função POST após alterar o valor da propriedade *employee.feature* para falso, e nesse caso a feature não deve ser ativida e o funcionário não deve ter o aumento de salário.

```java
@Test
public void givenFeaturePropertyFalse_whenIncreaseSalary_thenNoIncrease() 
  throws Exception {
    Employee emp = new Employee(1, 2000);
    employeeRepository.save(emp);
     
    System.setProperty("employee.feature", "false");
 
    mockMvc.perform(post("/increaseSalary")
      .param("id", emp.getId() + ""))
      .andExpect(status().is(200));
 
    emp = employeeRepository.findOne(1L);
    assertEquals("salary incorrect", 2000, emp.getSalary(), 0.5);
}
```

O próximo teste é alterando a proprieda *employee.feature* para true e nesse caso o salário do empregado deve ter um acréscimo.

```java
@Test
public void givenFeaturePropertyTrue_whenIncreaseSalary_thenIncrease() 
  throws Exception {
    Employee emp = new Employee(1, 2000);
    employeeRepository.save(emp);
    System.setProperty("employee.feature", "true");
 
    mockMvc.perform(post("/increaseSalary")
      .param("id", emp.getId() + ""))
      .andExpect(status().is(200));
 
    emp = employeeRepository.findById(1L).orElse(null);
    assertEquals("salary incorrect", 2200, emp.getSalary(), 0.5);
}
```

Para finalizar, nós vimos nesse artigo como utilizar a biblioteca *Togglz* junto com Sping Boot e como verificar se a toggle está ou não habilitada.

O código completo está em meu [GitHub](https://github.com/rpinheiroalmeida/feature-toggle-manager).

Para referências, você pode consultar:

* https://www.baeldung.com/spring-togglz
* https://www.togglz.org/documentation/activation-strategies.html#server-ip