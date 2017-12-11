#1.Introduce

  the project aims at sending weibo entirely automatically,you do not need to take code and the login process into consideration. you can communicate with weibo directly.
  But before using the software,the below is necessary:
  
  1.weibo account:username and password.
  2.app of weibo api paltform:app_key,app_secret and callback_url
  

 该软件包支持自动获取code，为用户提供微博API接口。



2,Project Structure

	 ├── setup.cfg
	├── setup.py
	├── weiborobot
	│   ├── auth.py    获得code后， 为client设置token
	│   ├── config.py   配置文件，配置了各种URL以及post请求时的表单数据
	│   ├── __init__.py
	│   ├── ticket4code.py   该类主要是要获得ticket，ticket是获得code的一个前提。
	│   ├── utils.py    提供加密算法
	│   └── weiborobot.py     封装好的robot类，提供一个更友好的HTTP方法，

 
 本软件包依赖于：sinaweibopy和requests,rsa等模块


3.Usage
  
   pip install weiborobot 
   
   
   
     from weiborobot import WeiboRobt

    robot = WeiboRobot('username','password','app_key','app_secret',callback_url=callback_url)
	text = 'wffwf'
	   robot.communicate('/statuses/share','post',status=text)
    print robot.communicate('/statuses/user_timeline','get')
