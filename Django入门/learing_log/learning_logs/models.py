from django.db import models

#模型就是一个类，包括属性和方法
class Topic(models.Model):
    '''用户学习的主题'''
    text=models.CharField(max_length=200) #CharField字符组成的数据即文本，还要设置max_length参数，规定主题名称的最大长度
    date_added=models.DateTimeField(auto_now_add=True) #DateTimeField日期时间类型，auto_now_add=True表示每次创建新主题时都自动添加当前时间

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
'''创建一个名为Topic的类，它继承了Model，即Django定义了模型基本功能的类，我们给Topic类添加了两个属性：text和date_added。每个属性都代表数据库中的一个字段。text是一个CharField，date_added是一个DateTimeField，后者记录了添加主题的时间。'''