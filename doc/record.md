# Bank lab

## 准备工作

### 使用venv，安装django、DRF

### 使用django-admin建立项目

在settings中增加drf，cors和时区、MySQL等的配置

## 后端

### Apps

- branch：银行信息
- client：客户信息
- account：账户信息

### Models

#### branch

- **BranchInfo**: 分行信息
- **StaffInfo**: 员工信息
- **DepartmentInfo**: 部门信息

#### client

- **ClientInfo**: 客户信息
- **ContactInfo**: 联系人信息
- **ClientStaff**: 客户与员工关系

#### account

- **AccountBase**: 账户基类
- **CheckingAccountInfo**: 支票账户
- **SavingsAccountInfo**: 储蓄账户
- **ClientAccount**: 客户-账户
- **LoanInfo**: 贷款信息
- **IssuranceInfo**: 贷款发放信息

### Views

通过我们的需求决定我们需要的views。

#### 客户管理(client)

> 提供客户所有信息的增、删、改、查功能;如果客户存在着关联账户或者贷款记录,则不允许删除。

