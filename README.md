
<a id="readme-top"></a>



<br />
<div align="center">
  <h1 align="center">🔐 {Webhook Protector} 🔐</h3>

  <p align="center">
    A simply way to avoid hard-coding your webhooks or risking a deletion.
    <br />
    <a href="https://github.com/yTax/webhook-protector/issues/new">Request Feature or report a bug</a>
  </p>
</div>
<div align="center">
    <a href="https://github.com/yTax/webhook-protector/graphs/contributors">
        <img src="https://img.shields.io/github/contributors/yTax/webhook-protector?style=flat-square" alt="Contributors" />
    </a>
    <a href="https://github.com/yTax/webhook-protector/network/members">
        <img src="https://img.shields.io/github/forks/yTax/webhook-protector?style=flat-square" alt="Forks" />
    </a>
    <a href="https://github.com/yTax/webhook-protector/stargazers">
        <img src="https://img.shields.io/github/stars/yTax/webhook-protector?style=flat-square" alt="Stars" />
    </a>
    <a href="https://github.com/yTax/webhook-protector/issues">
        <img src="https://img.shields.io/github/issues/yTax/webhook-protector?style=flat-square" alt="Issues" />
    </a>
</div>

    
    



# ⭐ 〢 Usage

This is a very simple script written in python that you can host anywhere, it has a very simple purpose which is ratelimitting and protecting your discord webhook from being deleted, this script will also be compatible with any other webhook integration.
It is implemented in a very basic way using Flask.  

To understand how to use this read [Getting Started](#-〢-getting-started)


# 🚀 〢 Getting Started

You can now choose if you want to install this on [Render](#-〢-installation-on-render) (Lifetime free hosting).

Or if you want to install it [on your server or local machine](#Installation-Local). By simply downloading the source files.


# 💻 〢 Installation on Render

1. Setup a [Render](https://dashboard.render.com/register) account.
2. [Fork](https://github.com/yTax/webhook-protector/fork) this repository (DONT FORGET TO MAKE THE REPOSITORY PRIVATE AND CHANGE THE KEY INSIDE MAIN.PY!!!).
3. Go to the [Dashboard](https://dashboard.render.com/select-repo?type=web) and click connect github.
4. Write `python main.py` as your start up command. Select Free as the instance type.
5. Setup the environment variables like this:
```
DISCORD_WEBHOOK_URL : Your_Webhook
SECRET_KEY : your_secret_key
```
6. Press "Deploy Web Service"
7. After your service is deployed grab it's URL on the dashboard, it should look something like: `https://webhook-protectorbzx4y.onrender.com`
7. Now we need to keep our Render server alive 24/7, to do this make an account on [CronJob](https://console.cron-job.org/signup)
8. After creating your account, go to the [Dashboard](https://console.cron-job.org/dashboard) and click Create CronJob.
9. Type whatever you want for the title and set your Render URL as the CrobJob URL.
10. Set the execution schedule to every 5 minutes.
11. Go into the Advanced tab and set a header with the key `Authorization` and value `KeepAlive`, finally change your request method to `POST`.
12. Done! Your webhook is now protected. The cronjob will keep the render server alive 24/7.

You can find a snippet that shows how you can incorporate this API into your code inside `runtest.py`.


