### cookies
关键值:  JSESSIONID

### 学生信息:
> ```http://stu.ityxb.com/back/bxg_anon/user/loginInfo```

请求无参数
返回参数键值
| 参数名 | 参数值 |
| ----- | ----- |
|nickname| 用户名|
|student_no|学号|


### 所学课程
> ```http://stu.ityxb.com/back/bxg/course/getHaveList```

请求参数：type=1&pageNumber=1&pageSize=10000
作用未明
返回参数关键值
| 参数名 | 参数值 |
| ----- | ----- |
| items | 课程列表对象 |
| id | 课程id |
| name | 课程名字|
| totalCount | 剩余任务数(猜测包括预习和作业) |

### 当前任务（预习、作业）
> ```http://stu.ityxb.com/back/bxg/user/getThreeRedPoints```

无请求参数
返回参数关键值
| 参数名 | 参数值 |
| ----- | ----- |
| preview | 预习任务数 |
| busywork | 未明，猜测有用|
| exam | 我猜是考试 |


### 任务信息查询
> ```http://stu.ityxb.com/back/bxg/user/unfinished```

请求参数： pageNumber=1&pageSize=10&type=1
猜测type为类型，1为预习
返回参数关键值
| 参数名 | 参数值 |
| ----- | ----- |
| id | 任务id |

### 预习任务章节获取
> ```http://stu.ityxb.com/back/bxg/preview/info```

请求参数: previewId=52847b3846e0491fbc064564e30f8214
| 参数名 | 参数值 |
| ----- | ----- |
| previewId | 任务查询获取的id |
返回参数关键值
| 参数名 | 参数值 |
| ----- | ----- |
| preview | 预习任务信息 |
| chapters | 预习任务章节信息 |
| point_id | 任务id(请求完成需要) |
| 返回数据比较复杂|需要自己请求再分析一下|


### 预习视频进度提交
> ```http://stu.ityxb.com/back/bxg/preview/updateProgress```

参数: previewId=52847b3846e0491fbc064564e30f8214&pointId=7529d9aeffe84cec97277f83b08e0d96&watchedDuration=1
| 参数名 | 参数值 |
| ----- | ----- |
| previewId | 任务查询获取的id  |
| pointId | 章节请求获取的id |
| watchedDuration | 当前观看的时间（观看进度）|
当前观看的时间可以直接设成9999，服务器会自动校准到最大值
返回参数
| 参数名 | 参数值 |
| ----- | ----- |
| resultObject|当前服务器记录观看时间(进度)|
| success | 是否更新成功 |

### 请求习题
> ```http://stu.ityxb.com/back/bxg/preview/questions```

请求参数:  questionspreviewId=52847b3846e0491fbc064564e30f8214&pointId=b74d5e37279c414cb6ed84d642a016a1
| 参数名 | 参数值 |
| ----- | ----- |
|questionspreviewId|等同于上面的previewId|
| pointId| 参考上面 |
返回参数关键值
| 参数名 | 参数值 |
| ----- | ----- |
| id| 问题id(下面要用)|



### 提交习题
(可重复请求，后面的请求会覆盖前面的)
所以可以先随便选一个答案，然后请求到正确答案之后再改
>```http://stu.ityxb.com/back/bxg/preview/ansQuestions```

请求参数:  previewId=52847b3846e0491fbc064564e30f8214&pointId=b74d5e37279c414cb6ed84d642a016a1&preivewQuestionId=8e980f2cdeac4b9e9db99eb0a98b5e4b&stuAnswer=0
| 参数名 | 参数值 |
| ----- | ----- |
| previewId | 参考上面|
| pointId | 同上|
| preivewQuestionId| 问题id|
| stuAnswer | 选项值 |
返回参数
| 参数名 | 参数值 |
| ----- | ----- |
| success | 是否成功 |


### 查看习题(要先做了才能看)
>``` http://stu.ityxb.com/back/bxg/preview/viewQuesAnsResult```

参数：previewId=52847b3846e0491fbc064564e30f8214&pointId=b74d5e37279c414cb6ed84d642a016a1
| 参数名 | 参数值 |
| ----- | ----- |
| previewId | 参考上面|
| pointId | 同上|
返回参数
| 参数名 | 参数值 |
| ----- | ----- |
| answer | 答案 |
| stuAns | 你选的答案|





