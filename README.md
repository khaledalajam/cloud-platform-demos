I'm preparing for the Azure Administrator AZ-104 certification as I transition into a Cloud Security Engineer role. I thought I'd document some of the core identity and cloud security principles with a focus on Microsoft Azure. 

To set the stage, the demos in this portfolio were built in a real Azure subscription named **Prima-Macula Prod Sub 1**, representing this fictional organization **Prima-Macula** within this environment. This is not a sandbox; it's a production-like Azure setup configured with industry-standard services and security controls.

Each demo begins with an overview diagram, and then walks through the implementation of a core security concept from setup to validation.

>**NOTE:** These are demonstrations, not step-by-step tutorials. Screenshots show key configurations and outcomes, the context and intent are explained in the text.


[Hybrid Identity & SSO](<Hybrid Identity with Seamless SSO.md>)

We're setting up hybrid identity between on-premises AD and Entra ID, with Seamless SSO for simplified user access.

[Privileged Access Management](<PAM Using Entra PIM.md>)


Privileged Identity Management (PIM) supports Azure RBAC roles, Entra ID roles, and group memberships. This demo focuses on Entra ID roles, which require Microsoft Entra ID P2 licensing to use PIM.



[Conditional Access](<Conditional Access Policy.md>)


We're going to create a simple conditional access policy for the pretend application registered within our Entra ID.



[Network Security Group](<Network Security Groups.md>) 

For this demo we're going to create and configure a network security group, or NSG for short, for our Windows VM to control the access to it.


>This portfolio demonstrates core cloud security principles through hands-on Azure implementations. These foundational skills are directly applicable across cloud platforms, including AWS and Google Cloud.


I'd welcome your feedback; feel free to reach out to me and let me know your thoughts about these demos and how they apply to real-world scenarios.
