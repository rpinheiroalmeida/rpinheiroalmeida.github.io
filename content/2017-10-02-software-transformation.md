---
layout: post
title: Agile transformation my first experience
modified: 2018-01-16 22:22
Category: Legacy code
tags: Lean Software, Agile, Transformation
comments: true
share: true
---
 
Although, for contractual reason I cannot say our client’s name. There are some interests facts I can talk, as:

* Our client is one of the oldest companies in the world. It was founded in the 1600s.
* It’s a big international e-commerce company, more specifically in the retail niche, with designer clothes.
* It’s not so famous here in Brazil, but in North America it’s very famous.
* In recent years it has stood out in the market through its acquisitions. Today, they have five known brands in the world market.

With each acquisition of news brands, the company wished to create a common platform, after all there are common business roles between brands, because the companies acquired are e-commerces with similar niches and market. Another factor is they want to keep the same or similar infra-structure for all brands, reducing licensing costs with new software, new team and of course, the main goal of any company, increase the billing and reduce costs.

So, at first time the purpose of our project was to accomplish of a new brand for that common platform. The problem is that common platform is a big legacy code since 1999, with a lot of changing during this period and countless workarounds. So, the final result is a code which any change is costly. To get an idea, a simple change has an average takes one week.

Then, our team didn't know anything about the legacy code, tools, used software and client culture. We didn't have any idea what is coming. Even if, the challenge was accepted. The first step was to do an inception in the client, with the goal of understanding the architecture of the little monster, client culture and set expectations.

As one result we figured out a high level of silos and hierarchy which was causing a huge overload in communication. Development team frequently depended on the infra-structure team, that happily copied settings from one machine to another, or needed to run in circles to fix defects that didn't exist, since the QA team had different process and with minimum interaction.

Another result we draw this image of all understanding, study and conversations.

<figure>
  <a href="/images/monolith.png">
  <img src="/images/monolith.png" alt="image"></a>
  <figcaption>Monolith's architecture.</figcaption>
</figure>

The main code is in the Blue Martini, that is a software, platform and/or api. Basically, Blue Martini it was a software manufacturer and professional services provider based in San Mateo, California that sold supported an e-commerce, contact center, relationship marketing, and clienteling applications to retailers and other consumer-facing companies.

Nowadays, we don't have more evolution in the product and what we discovery Blue Martini died in 2012. The company that bought Blue Martini declared that no intention of evolving it. Unfortunately, the most of our changes concentrates in this software and anyone of our team (involve client developers) knew it much. All was not lost, the legacy code are Java 1.6, Servlets, JSPs, a lot of JavaScript frameworks added with time, sometimes used and sometimes didn't used.

As search engine has been using Endeca, which is a database of indexing and search by data. This product was bought by Oracle and continues to evolve. Even if, to do somethings there it isn't so easy and any change needs a lot of discovering how the things work. This database is loaded through an ETL (it's a job responsible to extract data from a data source, transforming it according with the new database and, finally, loaded it in the new database).

Our client has full knowledge that the actual system no longer meets the needs and business evolution. It's so difficult and costly, both in time and in resources, to make changes and maintain the current system in reason of its complexity. Besides that, as I said above, Blue Martini had died and therefore didn't have support and evolution.

Then, in the face of all those problems the company wished to migrate and apply, step by step, a bottleneck strategy, creating a microservice architecture. Basically, the idea is to create microservices around the legacy and adding new business roles only in the microservice rather than to add in the legacy.

Ok, but how did we figured out all these things? How did we fix the chock culture with the client? And, how were our action items more productive? We did some actions related to that which has been showing good results.

Even with our client being remote, in another country, **we maintained a constant presence in the client**. It was a way of demonstrating that we weren't only a photo on Slack or an e-mail contact, we were people with feelings, goals and thoughts. Showing our presence, also we put our face to lid with the problems and find solutions together. In summary, also it's a way to create links between us and the client.

**Choose which battle we should fight**, which are really going to add something to the client and aren't just ego disputes. One example of that was the constant conflicts between ours QA and them. Our team together decided give something away, for example, some refactor, so that the team as a unit could buy discussions that would bring benefits to the QA process.

It was very important we **defined a plan for the transformation**. Some important questions we made was: What do we want transform? What's? What's bothering us in the process? What's the benefits and malfunctions of the pull request politics? Do we want increase the quality code with units tests? That transformation plan should be created and clear for all team, everyone has to be align with it.

**Prove that your strategies are coherent and makes sense**. Sometimes, the better way to prove something is simply doing and showing the results and its benefits. I remembered once, the client wanted us to use an old library to communicate with Soap instead of a new one. And the reason that the client used this was that library generates all the integration code. But the problem was the code generated was difficult to test and to do changes. So, we did the way we'd thought was the correct while another person discussed the solution with the client. Soon we finished, we showed the solution, they loved it and forgot completely the another library.

**Be persistent with what you believe to be the right and with the transformation plan**. Of course, always justifying the reason of your plan and decision.

**Create a collaborative team**. A real team isn't a group of people working together, but an unit with a common and well defined objective. I know that it isn't easy. Although we get a collaborative team. I believe one reason to get there was because the problem we had with the client, every discussion or conflicts we got stronger.

Those lessons we learned during and after the project. Some of them, we didn't even know what we were doing, discovering after analysis of our actions, success and fails.
