<img width="4054" height="2206" alt="Network Security Group (NSG)" src="https://github.com/user-attachments/assets/a498678f-b66c-44da-a3f5-1bc7e7ce60ce" />


For this demo we're going to create and configure a network security group, or NSG for short, for our Windows VM to control the access to it.

An important consideration for public IP address attached to resources in virtual networks, you'll see here within the overview of this public IP address that's attached to our VM, we've got the standard SKU, not the older basic SKU. Importantly for this, that means if we try and access any resource behind a standard public IP address, it's not going to work by default, because we need to configure a network security group to allow that access. 

Eventually this connection is going to fail. This demonstrates that by default now Microsoft is being more secure through the use of those standard SKU public IPs.

<img width="1920" height="816" alt="image" src="https://github.com/user-attachments/assets/9f0783b6-dd75-4b71-be24-b8ada73096c9" />

Network Security Groups have several default security rules that you can't edit or delete them. The only thing I can do is I can create new rules with a higher priority being a lower number to override them.

<img width="1920" height="1024" alt="image" src="https://github.com/user-attachments/assets/c50577c7-5dd3-4863-b42a-c9147c31df87" />

So by default I've got allow VNet connectivity inbound and outbound, I allow load balancer connectivity, and I also allow interent outbound, but otherwise you'll see I block everything else by default. So if you want something to be allowed you have to create an allow rule. And that's exactly what we'll do.

I'll create a rule that can allow us to remotely connect to that virtual machine.

<img width="1920" height="1026" alt="image" src="https://github.com/user-attachments/assets/642c38a3-0dbd-4ab4-8a49-5aa888db37f9" />
<img width="1920" height="1006" alt="image" src="https://github.com/user-attachments/assets/4b8f60d1-9e7a-4f89-88c3-b58541e407b8" />

You'll see now that we've got that rule there. It's sitting at the top of the list because I have the lower number than the other ones, meaning this rule will take priority.

<img width="1920" height="707" alt="image" src="https://github.com/user-attachments/assets/6b48b7b1-c587-4480-a1e5-37faf4082b94" />

I'll go ahead and apply this NSG. Currently it's just a security guard that's doing nothing, it's got some rules but it's not been told to go and guard any areas. To do that, we're going to have to associate this NSG, either to just the virtual machine network interface (NIC), or we could associate it to the subnet, and that's what we'll do.

<img width="1920" height="762" alt="image" src="https://github.com/user-attachments/assets/7d15d01b-5fa1-40d9-87c6-d57538ce4058" />

We've got that NSG ready to go, in fact if we take a look at that virtual machine, vm1, and look at the network interface card, you'll see I can get a breakdown of the NSG rules that apply to this virtual machine.
So we do see that it applies. 

<img width="1920" height="1012" alt="image" src="https://github.com/user-attachments/assets/825ef3a4-cdee-4a70-8fe7-cd5d456cf164" />

We do see that inbound RDP is allowed, and that should mean that if we go back to my RDP client, we can now connect.

<img width="1920" height="1027" alt="image" src="https://github.com/user-attachments/assets/aa0a36fc-3f54-4d52-ad33-9ec2240b257b" />

We've got that NSG up and working.

<img width="1920" height="1079" alt="image" src="https://github.com/user-attachments/assets/a057465c-d74a-4d19-8db6-26c68fcf4dc9" />









