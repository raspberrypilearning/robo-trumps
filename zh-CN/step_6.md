## 随机显示一个机器人

让我们添加代码，以便在您键入Random而不是一个机器人名称的时候获得一个随机机器人。

+ 首先，您将需要从随机模块中导入choice函数：
    
    ![截图](images/robotrumps-random.png)

+ 您可以使用`choice`从机器人字典的键表中选择一个随机机器人名称。
    
    ![截图](images/robotrumps-choice.png)

+ 在Python 3中，您需要使用`list`将`keys`的结果放进入列表中。
    
    提示：请确保您已认真检查您的括号！