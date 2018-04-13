## 显示数据

现在你可以用更有趣的方式来显示机器人数据。 

让我们显示一张带有图片及机器人智能和实用性数据的机器人王牌卡。 

你完成此步骤以后，你将能够如下所示来显示机器人：

![screenshot](images/robotrumps-example.png)




+ 询问用户他们想看到哪个机器人：

  ![screenshot](images/robotrumps-choose.png)
  
+ 如果机器人存在于字典中，则查找其数据：

  ![screenshot](images/robotrumps-if.png)
  
  输入一个机器人的名称来测试你的代码。

  
+ 如果机器人不存在，会出现一个错误：

  ![screenshot](images/robotrumps-else.png)
  
 输入字典中不存在的机器人名称来测试你的代码。

+ 现在你要使用 Python 海龟来显示机器人数据。 

  在你的脚本顶部导入海龟库，并设置画面和海龟：

  ![screenshot](images/robotrumps-turtle.png)

+ 现在添加代码来使海龟打印出机器人的名称：

  ![screenshot](images/robotrumps-name.png)
  
+ 尝试更改 `style` 变量直至你对文本满意。 
  
  除了 `Arial`，你还可以尝试：`Courier`、`Times` 或 `Verdana`。 
  
  将 `14` 更改为不同的数字来更改字体大小。 
  
  你可以将 `bold`（粗体）更改为 `normal`（正常）或 `italic`（斜体）。 
  
+ 将机器人的统计数据列表储存在变量中，而不是将其打印输出：

  ![screenshot](images/robotrumps-stats.png)
  
+ 你现在可以将机器人的统计数据作为列表中的项目进行访问：

  + `stats[0]` 指智能
  + `stats[1]` 指电池
  + `stats[2]` 指图片名称
  
  添加代码来显示智能和电池统计数据：
  
  ![screenshot](images/robotrumps-stats-2.png)
   
  
+ 噢天哪！统计数据全都堆在了一起。你将需要添加代码来移动海龟：

   ![screenshot](images/robotrumps-stats-3.png)

+ 最后，让我们添加机器人图片来完成显示。 

  从 `cards.txt` 读取数据时，你将需要新增一行来注册图片：
  
  ![screenshot](images/robotrumps-register.png)
     
+ 然后添加代码来定位和标记图片：

  ![screenshot](images/robotrumps-image.png)
  
+ 输入一个机器人然后再输入另一个来测试你的代码，你会看到他们相互叠加在一起！

  你需要在显示一个机器人之前清空屏幕： 

  ![screenshot](images/robotrumps-clear.png)



