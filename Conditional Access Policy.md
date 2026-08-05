<img width="2104" height="1332" alt="Entra ID Conditional Access" src="https://github.com/user-attachments/assets/f4470d63-8e9b-4de4-95d7-3723dd14fd7c" />


We're going to create a simple Conditional Access Policy for the pretend application registered within our Entra ID.

We'll start by showing how we can use locations. Locations is one of the key components of Conditional Access that makes you consider where are your solutions being accessed from. There's a couple of ways we can configure locations.

Say we want to consider when applications are being accessed from the GCC location. What we're talking about for country locations is determining the location that access to our solution originates from either using IP address or by using GPS coordinates. So if we create this location we can use that within our access policies.

<img width="1919" height="822" alt="image" src="https://github.com/user-attachments/assets/20828020-6f8a-4a2b-92a5-f2070f59fe2a" />

Commonly what I might also want to do is create my own location, and if I wanted to, I do also get the option to tick whether this location is considered as trusted. 

<img width="1919" height="616" alt="image" src="https://github.com/user-attachments/assets/2a0d870d-999f-44c9-abad-59f5bc573661" />

And then what we can do within our access policies is say what we want to do with trusted versus untrusted locations.

<img width="1919" height="643" alt="image" src="https://github.com/user-attachments/assets/ffe159e5-6c72-4e6f-86bb-afa35aec00b1" />

Before we go ahead and create our access policy, if you're using a new Entra tenant, like in my case here, i did want to mention that it's quie likely you'll have Security Defaults enabled. So if you want to use conditional access policies, you'll have to switch those off.

<img width="1333" height="726" alt="security defaults" src="https://github.com/user-attachments/assets/6a30de49-8c43-41a1-a62c-7b95175194cc" />

For Target resources, we'll choose our HR application Macula HR App.

<img width="1919" height="1038" alt="image" src="https://github.com/user-attachments/assets/b34d49ae-85d3-4020-ad4f-b4f1f5a216c3" />

What you might choose to do in Conditions is say any location and then exclude your trusted locations. GCC and Head Office in this case. 

<img width="1919" height="1035" alt="image" src="https://github.com/user-attachments/assets/6a61fc04-a17a-4970-aeb8-6d798e78a0a7" />

Or maybe it's locations that you have already marked as trusted. So that's what we'll go ahead and do. We'll say we want to exclude all trusted locations, but otherwise look at every single location and then impose these conditions.

<img width="1919" height="1031" alt="image" src="https://github.com/user-attachments/assets/2d673fb4-d558-497a-8a2f-ca1892b53986" />

So what we have now is a conditional access policy applying to all users, for our HR app, with MFA required, but it's not going to apply if it's the trusted location.

And we've completed our Conditional Access Policy. There's a final option to do with Reporting, On or Off. It is encouraged if you're using conditional access policies is to use Report-only first.

What this means is that CAP will be there behind the scenes running for all your authentications. You can go in and check the logs to see what would happen and whether access would be allowed or denied. Once you're happy that it's ready to go, you can switch it to On and your conditional access will take effect.

<img width="1917" height="1034" alt="image" src="https://github.com/user-attachments/assets/e7d03972-1148-4fed-92ae-8abab13e24ba" />

We've created a conditional access policy that uses a named location.

<img width="1919" height="630" alt="image" src="https://github.com/user-attachments/assets/260c2dd3-a43b-4ef3-9275-3d436e5f21fa" />

If we did want to understand what might happen under certain conditions we can use the What-if section. What-if is a handy tool that helps you to understand what's going to happen when you have one or more conditional access policies. 

What-If is going to go through using all of those settings that I have defined, and check to see what would happen in that condition. 

<img width="1919" height="1031" alt="image" src="https://github.com/user-attachments/assets/ecd30abb-65e3-4dca-a92f-1b077d82d77b" />

In this scenario, no policies would apply.

<img width="1251" height="689" alt="no policies applied what-if" src="https://github.com/user-attachments/assets/bcd13da4-ea91-4ee5-8d4b-25750a5dc531" />

However, if we go back and say that the IP address isn't 1.2.3.4, it's in fact 1.1.1.1. And this time the access policy will apply. 

<img width="1381" height="762" alt="what-if applies" src="https://github.com/user-attachments/assets/b26e1aa8-5d5f-48dd-ad1c-734e5a515049" />

So we have seen that our access policy is working. We know that if Ahmed tries to log in from 1.2.3.4, the policy won't apply, and that's because we had that as a trusted location that was exlcuded. 





