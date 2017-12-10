"""
weiborobot
-----

Notice:

1.it is built on sinaweibopy ,so it only supports python2.7 or python2.6.

2.everything should be encoded in unicode.


the lib make you can send weibo entirly automatically.instead of getting code
by url in the browser.
you just input

   1.your weibo account:username and password
   2.app:app_key,app_secret

````````````


Save in a hello.py:

.. code:: python

    #-*-coding:utf-8-*-

    from weiborobot import WeiboRobt

    robot = WeiboRobot('username','password','app_key','app_secret',callback_url=callback_url)
	text = 'wffwf'
	robot.communicate('/statuses/share','post',status=text)
    print robot.communicate('/statuses/user_timeline','get')


And Easy to Setup
`````````````````

And run it:

.. code:: bash

    $ pip install weiborobot



Links
`````
* `development version
  <https://github.com/haipersist/weibo>`_

"""

from setuptools import setup



setup(
    name='weiborobot',
    version='1.1.3',
    url='https://github.com/haipersist/weibo',
    license='BSD',
    author='Haibo Wang',
    author_email='393993705@qq.com',
    description='A weibo api for sending weibo automatically',
    long_description=__doc__,
    packages=['weiborobot'],
    #package_dir={'weiborobot': 'weiborobot'},
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'requests>=2.8.1',
        'rsa',
        'sinaweibopy'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],

)
