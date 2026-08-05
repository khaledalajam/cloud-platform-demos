<img width="2107" height="1430" alt="Hybrid Identity   SSO" src="https://github.com/user-attachments/assets/012aceef-2f39-4b25-9438-7d2d1c52664a" />


What we're doing in this demo is setting up hybrid identity between our on-premises Active Directory domain and our Entra ID tenant. Additionally we are going to configure seamless single sign on (SSO) to allow for our users to easily access Entra resources using their AD identity, with less prompts for logging in. 

For that to work, I am going to have a pretend Active Directory Domain services forest, which I do have that already setup.

<img width="1918" height="825" alt="image" src="https://github.com/user-attachments/assets/da64cd74-1552-414b-a8ac-f5eab85c6bc0" />

I will be using the Entra Administration Center. What we're going to do within this demo is configure Cloud-Sync, and to do so we're going to setup an agent on our existing domain controller. This is currently running on a virtual machine in Azure, probably more likely in the real world to be running on-premises. Wherever this is we want to go and make sure that we've got that agent installed on a machine that has access to this domain controller, for demonstration purposes we're just going to install that directly on the domain controller.

That is the domain that we want. Everything ready to go for this provisioning agent to synchornize identities from on-premises to the cloud. When using Entra Connect Cloud-Sync, it's in the name, just an agent to sync to the cloud. The configuration is going to take place within the portal.

<img width="1919" height="1027" alt="image" src="https://github.com/user-attachments/assets/212721d8-d581-46f6-bfcc-1d5965a0247d" />

The agent has been installed and ready to go. Time to set up that configuration.

<img width="1919" height="483" alt="image" src="https://github.com/user-attachments/assets/53161bca-e6e4-4195-a023-e3f6f88d8e5e" />

We can see the domain that we've just configured the agent for. We can also choose password hash sync, which ensures that a hash of the password is synchrnized with Entra and that can be used with other features such as identity protection and some other services.

<img width="1142" height="490" alt="image" src="https://github.com/user-attachments/assets/b2a20747-6771-4d2f-84b9-5bc66fd0e1fd" />

Configuration deployed.

<img width="1919" height="677" alt="image" src="https://github.com/user-attachments/assets/31d01519-4bdb-4b69-bd0b-51b108365351" />

We now have Elliot Alderson, our user account from our on-premises active directory that we can see here is synchronized. 

<img width="1919" height="618" alt="image" src="https://github.com/user-attachments/assets/e5769ed4-4eea-4d36-829e-de346b1cb490" />

Since we're using Cloud-Sync we have to do things a bit manually and enable seamless single sign-on for our tenant using the MSI and some commands.

We see on screen that we're successfully connected to our on-premises Active Directory enviroment and ready to go and enable SSO for our Entra ID tenant.

<img width="1919" height="1030" alt="image" src="https://github.com/user-attachments/assets/ec7428f8-6f50-4907-811c-09097e1b00df" />

Local internet is the setting that we will need to configure if we want to use seamless single sign on for our users, along with enabling "Allow status bar updates via script". 

<img width="449" height="607" alt="image" src="https://github.com/user-attachments/assets/859cf8cf-f4be-49cb-9eee-920952717501" />

I'm going to myapps.microsoft.com/ entering my domain name. What this means is as soon as I hit enter this website is going to go to the myapps portal for my organization, and so it's got all the information that needs to know where we're trying to log in. 

<img width="1919" height="622" alt="image" src="https://github.com/user-attachments/assets/b8d83538-37b4-45a8-8fdb-0f44394d0c4d" />

Straight into the myapps portal. That is the seamless single sign-on experience for our users.

<img width="1919" height="1029" alt="image" src="https://github.com/user-attachments/assets/310bc004-5868-48d6-ad84-810a92d1a0d4" />

In fact, going back to the Entra Admin Center we see seamless single sign on enabled for my enviroment. Also having configured those user settings with internet security and the status bar update to ensure that auto login experience is seamless.

<img width="1915" height="741" alt="image" src="https://github.com/user-attachments/assets/330c7c67-814e-429a-9798-3af0d67c2500" />





