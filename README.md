# Sinker
Setting up a phishing campaign isn't easy. You have to tailor your ruse to your target, capture credentials, make sure your domain isn't so new it will be blocked, etc. This program solves some of the above challenges.

This program was built for authorized pentesters and educational purposes. The author does not condone the use of this software to aid or assist in malicious activity.

## Requirements
* an internet accessible server
* a domain with A records pointing at that server
* an IPinfo api token 

## Instructions ##
1. replace the ip address in the inventory file with the IP of your server.
2. If you do not have ansible installed on your local machine run runme_first.sh
install ansible if it is not installed on your local machine. If you make a mistake, you can run the script again, OR make the changes directly in the vars.yml file.
3. Change the necessary configuration variables in vars.yml
4. Run the command: `ansible-playbook main.yml`

## Acknowledgments ##
The example html form is using [this](https://tympanus.net/Tutorials/LoginRegistrationForm/index3.html#toregister) template.
