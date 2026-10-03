I'm building out a platform engineering skill-set on top of my IT infrastructure and security background. This portfolio documents hands-on work across CI/CD and containerization and cloud identity/security.

The container demo demonstrates the full build-to-deploy lifecycle: Dockerfile → CI/CD → registry → local run.

The Azure demos were built in a real Azure subscription (Prima-Macula Prod Sub 1) representing a fictional organization.


>**NOTE:** This is not a sandbox; it's a production-like setup with industry-standard services and security controls. These are demonstrations, not step-by-step tutorials; screenshots show key configurations and outcomes; the context and intent are explained in the text.

[Container Build & Deployment](<Container Build & Deployment.md>)

For this demo we're containerizing a minimal Python service and automating the full build-to-deploy pipeline.

[Hybrid Identity & SSO](<Hybrid Identity with Seamless SSO.md>)

We're setting up hybrid identity between on-premises AD and Entra ID, with Seamless SSO for simplified user access.

[Privileged Access Management](<PAM Using Entra PIM.md>)


Privileged Identity Management (PIM) supports Azure RBAC roles, Entra ID roles, and group memberships. This demo focuses on Entra ID roles, which require Microsoft Entra ID P2 licensing to use PIM.



[Conditional Access](<Conditional Access Policy.md>)


We're going to create a simple conditional access policy for the pretend application registered within our Entra ID.



[Network Security Group](<Network Security Groups.md>) 

For this demo we're going to create and configure a network security group, or NSG for short, for our Windows VM to control the access to it.


>This portfolio demonstrates cloud security and platform engineering principles through hands-on implementations. These skills are directly applicable across cloud platforms, including AWS and Google Cloud.

I'd welcome your feedback; feel free to reach out and let me know your thoughts on how these apply to real-world scenarios.
