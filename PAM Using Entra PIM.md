
<img width="894" height="486" alt="Entra PIM" src="https://github.com/user-attachments/assets/2af86aeb-3a91-4078-a1ed-9b18c5fe45a1" />

Privileged Identity Management works with several different types of resources. It can be Azure Role Based Control roles, it can be Entra ID roles and also group membership. However, within this demo I'm going to focus on Entra ID roles, and we're going to need Entra Premium licensing since it is required.

<img width="1185" height="619" alt="Drawing 2026-02-06 22 55 36 excalidraw" src="https://github.com/user-attachments/assets/e0cf03db-43b0-4eda-996a-ae0ea1668459" />


What we'll do in this demo is we'll assign elegibility for an application administrator role to one of our users. 

Since we have the licensing and we've got PIM enabled, you'll see we can configure Pirvileged Identity Management. This is really what we are talking about right here.

<img width="1919" height="1035" alt="image" src="https://github.com/user-attachments/assets/f978858c-5430-4da8-88e5-4dd018e9420f" />

We can go ahead and say active and say permenantly assigned, and that will just mean that we're skipping PIM. 

If you didn't have PIM,then this is what what you are actually configuring when you create a role assignment. That it's going to always be permenantly active. 

<img width="1919" height="1029" alt="image" src="https://github.com/user-attachments/assets/872dd296-bdd7-4f24-bccd-5f325405d9ad" />

However, as we know, we want to protect these privileges, and so that's where we can configure elegibitliy.

We might allow our users to have elegibiltiy for this role always, being a part of their job, or maybe they're just working on a specific project for a period of time and we want to lock down this elegibiltiy.

<img width="1919" height="1027" alt="image" src="https://github.com/user-attachments/assets/31c10ef5-8d84-47be-9bfe-54c43009df09" />

What you've seen is that we've added a few extra controls to ensure that Ahmed can only elevate to permissions according to the settings we've defined here.

<img width="1919" height="643" alt="image" src="https://github.com/user-attachments/assets/baee5643-e0cc-473f-8a82-24630996605d" />

But what if you had some additional controls you wanted to implement ? Well, you can brows into the role settings for each of your roles, and we can configure all sorts of controls, like whether MFA is required, justification, maybe we do want approval before the role can be activated. 

<img width="1919" height="1036" alt="image" src="https://github.com/user-attachments/assets/50c602e5-2877-40a3-8787-9cfa2af41753" />

What we're talking about is a range of different controls that we can configure on a per role basis, and we can also configure on a per assignment basis to determin what people should be doing before they can activate those roles.

So we've got everything ready to go. What we now want to do is log in as our endpoint users to test this out. 

You'll see I'm logged in as Ahmed Abdullah. Now remember, Ahmed Abdullah has just been assigned eligibility for the application administrator role for our specfic app.

<img width="1919" height="1026" alt="image" src="https://github.com/user-attachments/assets/a797448e-d38a-4e17-bbbc-7455258e01ac" />

Right now we would expect that Ahmed doesn't have permissions to do anything with this app.

<img width="1919" height="883" alt="image" src="https://github.com/user-attachments/assets/2ab2a336-9b33-4023-a85f-dbba9e2d5ed8" />

So this is PIM, we've assigned eliglibility for permissions, but permissions aren't always active. To activate those permissions, Ahmed has to go to My roles section that got the different types of privilegs we might be activating, and we've got that Application Administrator role that Ahmed is eligible for.

Now that role is submitted for approval. And what we need to do is log into our approvers account and complete that approval.

<img width="1919" height="521" alt="activsate" src="https://github.com/user-attachments/assets/44291f0d-491c-4f41-8811-7883af93d391" />

You'll see that I'm logged in as Noura Khalid, our approver, and we've got Ahmed Abdullah's request for activation of that application administrator role.

<img width="1919" height="736" alt="image" src="https://github.com/user-attachments/assets/66a8a55e-5494-4905-900c-22406b835a48" />

Ahmed Abdullah's activation is complete.

<img width="1919" height="1035" alt="image" src="https://github.com/user-attachments/assets/593f7d72-aef7-4ef3-a92b-38eca0c2434b" />
<img width="1917" height="745" alt="image" src="https://github.com/user-attachments/assets/36b19282-962c-499d-aa94-5ba59628c9de" />

If we go back to Ahmed's page, we can expect to see that Ahmed has that activation complete in the active assignment section.

<img width="1919" height="502" alt="image" src="https://github.com/user-attachments/assets/a46def24-aa1a-4db3-90be-0d8f6434adbf" />

Now this time we can expect Ahmed can go to something like secrets and certifcates and the permissions has been activated. So we can create a new secret for example.

<img width="1917" height="836" alt="image" src="https://github.com/user-attachments/assets/d1deab75-a22c-4d63-9467-2f4883a558c8" />

You can see now we have those permissions active for Ahmed's account. And once complete, you can either wait for that to automatically expire, or Ahmed could go and just deactivate that assignment once complete.

<img width="1918" height="1029" alt="image" src="https://github.com/user-attachments/assets/a261e642-151d-49f6-bf3f-5fcbf37bf4e3" />




















