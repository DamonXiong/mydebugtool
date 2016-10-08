
# DebugTool 使用说明 #
## 选项填写说明 ##
### 1.Src Path ###
> 源代码所在目录全路径,biz-前一个路径

### 2.Dir Name ###
> Pos机上/Share/UmsTssMaster/resource/目录后的操作员目录名称八位数字如:00000001

### 3.Pull Path ###
> 需要导出设备上的相关信息,该信息存放的路径,全路径

## 按钮功能说明 ##
### 1.Pull ###
> 将Src Path目录下在内容Push到设备/Share/UmsTssMaster/resource/{Dir Name}目录下

### 2.Clear Cache ###
> 清除缓存,相当于调用pm clear com.ums.tss.mastercontrol

### 3.Clear Source ###
> 清除设备/Share/UmsTssMaster/resource/{Dir Name}目录

### 4.Clear DB ###
> 清除设备/Share/UmsTssMaster/storage/{Dir Name}目录

### 5.Pull DB ###
> 将设备上设备/Share/UmsTssMaster/storage/{Dir Name}目录下的内容导出到{Pull Path}\DB目录下

### 6.Pull Src ###
> 将设备上设备/Share/UmsTssMaster/resource/{Dir Name}目录下的内容导出到{Pull Path}\src目录下

### 7.Pull Sharelibs ###
> 将设备上设备/Share/UmsTssMaster/resource/sharelibs目录下的内容导出到{Pull Path}\sharelibs目录下

### 8.Clear Console ###
> 清除提示框中的信息