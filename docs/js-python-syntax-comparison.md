# JavaScript vs Python 语法对比指南

作为前端工程师，你已经熟悉了 JavaScript 的语法。本文档将通过对比 JavaScript 和 Python 的核心语法，帮助你快速掌握 Python 编程。

## 📋 目录

1. [基础语法](#基础语法)
2. [变量和数据类型](#变量和数据类型)
3. [运算符](#运算符)
4. [控制流](#控制流)
5. [函数](#函数)
6. [数据结构](#数据结构)
7. [面向对象编程](#面向对象编程)
8. [异步编程](#异步编程)
9. [模块和导入](#模块和导入)
10. [错误处理](#错误处理)
11. [常用内置方法](#常用内置方法)
12. [现代语法特性](#现代语法特性)

## 基础语法

### 注释

| JavaScript | Python |
|------------|--------|
| `// 单行注释` | `# 单行注释` |
| `/* 多行注释 */` | `"""多行注释"""` 或 `'''多行注释'''` |

```javascript
// JavaScript
// 这是单行注释
/* 
这是多行注释
可以跨越多行
*/
```

```python
# Python
# 这是单行注释
"""
这是多行注释
可以跨越多行
"""
```

### 语句结束

| JavaScript | Python |
|------------|--------|
| 分号 `;` （可选） | 换行符（必须） |
| 花括号 `{}` 定义代码块 | 缩进定义代码块 |

```javascript
// JavaScript
if (true) {
    console.log('Hello');
    console.log('World');
}
```

```python
# Python
if True:
    print('Hello')
    print('World')
```

## 变量和数据类型

### 变量声明

| JavaScript | Python |
|------------|--------|
| `var name = 'John'` | `name = 'John'` |
| `let age = 25` | `age = 25` |
| `const PI = 3.14` | `PI = 3.14` （约定大写表示常量） |

```javascript
// JavaScript
var name = 'John';        // 函数作用域
let age = 25;             // 块作用域
const PI = 3.14159;       // 常量
```

```python
# Python
name = 'John'             # 动态类型
age = 25                  # 自动推断类型
PI = 3.14159              # 约定大写表示常量
```

### 基本数据类型

| 类型 | JavaScript | Python |
|------|------------|--------|
| 字符串 | `'hello'` 或 `"hello"` | `'hello'` 或 `"hello"` 或 `'''hello'''` |
| 数字 | `42`, `3.14` | `42`, `3.14` |
| 布尔值 | `true`, `false` | `True`, `False` |
| 空值 | `null`, `undefined` | `None` |
| 数组/列表 | `[1, 2, 3]` | `[1, 2, 3]` |
| 对象/字典 | `{key: 'value'}` | `{'key': 'value'}` |

```javascript
// JavaScript
let str = 'Hello World';
let num = 42;
let float = 3.14;
let bool = true;
let empty = null;
let undef = undefined;
let arr = [1, 2, 3];
let obj = {name: 'John', age: 25};
```

```python
# Python
str_val = 'Hello World'
num = 42
float_val = 3.14
bool_val = True
empty = None
list_val = [1, 2, 3]
dict_val = {'name': 'John', 'age': 25}
```

### 类型检查

```javascript
// JavaScript
typeof 'hello'           // 'string'
typeof 42                // 'number'
typeof true              // 'boolean'
Array.isArray([1,2,3])   // true
```

```python
# Python
type('hello')            # <class 'str'>
type(42)                 # <class 'int'>
type(True)               # <class 'bool'>
isinstance([1,2,3], list) # True
```

## 运算符

### 算术运算符

| 运算 | JavaScript | Python |
|------|------------|--------|
| 加法 | `+` | `+` |
| 减法 | `-` | `-` |
| 乘法 | `*` | `*` |
| 除法 | `/` | `/` （浮点除法）, `//` （整数除法） |
| 取余 | `%` | `%` |
| 幂运算 | `**` | `**` |

```javascript
// JavaScript
10 / 3    // 3.3333333333333335
10 % 3    // 1
2 ** 3    // 8
```

```python
# Python
10 / 3    # 3.3333333333333335
10 // 3   # 3 (整数除法)
10 % 3    # 1
2 ** 3    # 8
```

### 比较运算符

| 运算 | JavaScript | Python |
|------|------------|--------|
| 等于 | `==` (类型转换), `===` (严格相等) | `==` |
| 不等于 | `!=`, `!==` | `!=` |
| 大于 | `>` | `>` |
| 小于 | `<` | `<` |
| 大于等于 | `>=` | `>=` |
| 小于等于 | `<=` | `<=` |

### 逻辑运算符

| 运算 | JavaScript | Python |
|------|------------|--------|
| 与 | `&&` | `and` |
| 或 | `||` | `or` |
| 非 | `!` | `not` |

```javascript
// JavaScript
true && false   // false
true || false   // true
!true          // false
```

```python
# Python
True and False  # False
True or False   # True
not True       # False
```

## 控制流

### 条件语句

```javascript
// JavaScript
if (age >= 18) {
    console.log('成年人');
} else if (age >= 13) {
    console.log('青少年');
} else {
    console.log('儿童');
}

// 三元运算符
let status = age >= 18 ? '成年人' : '未成年人';
```

```python
# Python
if age >= 18:
    print('成年人')
elif age >= 13:
    print('青少年')
else:
    print('儿童')

# 三元运算符
status = '成年人' if age >= 18 else '未成年人'
```

### 循环

#### for 循环

```javascript
// JavaScript
// 传统 for 循环
for (let i = 0; i < 5; i++) {
    console.log(i);
}

// for...of 循环（数组）
for (let item of [1, 2, 3]) {
    console.log(item);
}

// for...in 循环（对象）
for (let key in {a: 1, b: 2}) {
    console.log(key);
}
```

```python
# Python
# range 循环
for i in range(5):
    print(i)

# 遍历列表
for item in [1, 2, 3]:
    print(item)

# 遍历字典
for key in {'a': 1, 'b': 2}:
    print(key)

# 同时获取索引和值
for i, item in enumerate([1, 2, 3]):
    print(i, item)
```

#### while 循环

```javascript
// JavaScript
let i = 0;
while (i < 5) {
    console.log(i);
    i++;
}
```

```python
# Python
i = 0
while i < 5:
    print(i)
    i += 1
```

### 循环控制

| JavaScript | Python |
|------------|--------|
| `break` | `break` |
| `continue` | `continue` |

## 函数

### 函数定义

```javascript
// JavaScript
// 函数声明
function greet(name) {
    return `Hello, ${name}!`;
}

// 函数表达式
const greet2 = function(name) {
    return `Hello, ${name}!`;
};

// 箭头函数
const greet3 = (name) => `Hello, ${name}!`;
const add = (a, b) => a + b;
```

```python
# Python
# 函数定义
def greet(name):
    return f"Hello, {name}!"

# Lambda 函数（匿名函数）
greet2 = lambda name: f"Hello, {name}!"
add = lambda a, b: a + b
```

### 参数

```javascript
// JavaScript
// 默认参数
function greet(name = 'World') {
    return `Hello, ${name}!`;
}

// 剩余参数
function sum(...numbers) {
    return numbers.reduce((a, b) => a + b, 0);
}

// 解构参数
function createUser({name, age}) {
    return {name, age};
}
```

```python
# Python
# 默认参数
def greet(name='World'):
    return f"Hello, {name}!"

# 可变参数
def sum_numbers(*numbers):
    return sum(numbers)

# 关键字参数
def create_user(name, age, **kwargs):
    return {'name': name, 'age': age, **kwargs}

# 调用时指定参数名
create_user(name='John', age=25)
```

### 作用域

```javascript
// JavaScript
let globalVar = 'global';

function outer() {
    let outerVar = 'outer';
    
    function inner() {
        let innerVar = 'inner';
        console.log(globalVar, outerVar, innerVar);
    }
    
    return inner;
}
```

```python
# Python
global_var = 'global'

def outer():
    outer_var = 'outer'
    
    def inner():
        inner_var = 'inner'
        print(global_var, outer_var, inner_var)
    
    return inner
```

## 数据结构

### 数组/列表

```javascript
// JavaScript
let arr = [1, 2, 3, 4, 5];

// 添加元素
arr.push(6);              // 末尾添加
arr.unshift(0);           // 开头添加

// 删除元素
arr.pop();                // 删除末尾
arr.shift();              // 删除开头

// 访问元素
console.log(arr[0]);      // 第一个元素
console.log(arr[-1]);     // undefined (不支持负索引)

// 切片
arr.slice(1, 3);          // [2, 3]

// 遍历
arr.forEach(item => console.log(item));
```

```python
# Python
list_val = [1, 2, 3, 4, 5]

# 添加元素
list_val.append(6)        # 末尾添加
list_val.insert(0, 0)     # 指定位置添加

# 删除元素
list_val.pop()            # 删除末尾
list_val.pop(0)           # 删除指定位置

# 访问元素
print(list_val[0])        # 第一个元素
print(list_val[-1])       # 最后一个元素（支持负索引）

# 切片
list_val[1:3]             # [2, 3]
list_val[:2]              # [1, 2]
list_val[2:]              # [3, 4, 5]

# 遍历
for item in list_val:
    print(item)
```

### 对象/字典

```javascript
// JavaScript
let obj = {
    name: 'John',
    age: 25,
    city: 'New York'
};

// 访问属性
console.log(obj.name);        // 点记法
console.log(obj['age']);      // 括号记法

// 添加/修改属性
obj.email = 'john@example.com';
obj['phone'] = '123-456-7890';

// 删除属性
delete obj.city;

// 遍历
for (let key in obj) {
    console.log(key, obj[key]);
}

// 获取键值
Object.keys(obj);             // ['name', 'age', 'email', 'phone']
Object.values(obj);           // ['John', 25, 'john@example.com', '123-456-7890']
Object.entries(obj);          // [['name', 'John'], ['age', 25], ...]
```

```python
# Python
dict_val = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

# 访问属性
print(dict_val['name'])       # 括号记法
print(dict_val.get('age'))    # get 方法（安全访问）

# 添加/修改属性
dict_val['email'] = 'john@example.com'
dict_val['phone'] = '123-456-7890'

# 删除属性
del dict_val['city']
# 或者
dict_val.pop('city', None)    # 安全删除

# 遍历
for key in dict_val:
    print(key, dict_val[key])

# 或者
for key, value in dict_val.items():
    print(key, value)

# 获取键值
list(dict_val.keys())         # ['name', 'age', 'email', 'phone']
list(dict_val.values())       # ['John', 25, 'john@example.com', '123-456-7890']
list(dict_val.items())        # [('name', 'John'), ('age', 25), ...]
```

### 集合

```javascript
// JavaScript
let set = new Set([1, 2, 3, 3, 4]);

// 添加元素
set.add(5);

// 删除元素
set.delete(1);

// 检查元素
set.has(2);               // true

// 大小
set.size;                 // 4

// 遍历
for (let item of set) {
    console.log(item);
}
```

```python
# Python
set_val = {1, 2, 3, 4}    # 或者 set([1, 2, 3, 3, 4])

# 添加元素
set_val.add(5)

# 删除元素
set_val.remove(1)         # 如果不存在会报错
set_val.discard(1)        # 如果不存在不会报错

# 检查元素
2 in set_val              # True

# 大小
len(set_val)              # 4

# 遍历
for item in set_val:
    print(item)
```

## 面向对象编程

### 类定义

```javascript
// JavaScript (ES6+)
class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    
    greet() {
        return `Hello, I'm ${this.name}`;
    }
    
    static fromString(str) {
        const [name, age] = str.split(',');
        return new Person(name, parseInt(age));
    }
}

// 继承
class Student extends Person {
    constructor(name, age, grade) {
        super(name, age);
        this.grade = grade;
    }
    
    study() {
        return `${this.name} is studying`;
    }
}

// 使用
const person = new Person('John', 25);
const student = new Student('Alice', 20, 'A');
```

```python
# Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f"Hello, I'm {self.name}"
    
    @classmethod
    def from_string(cls, string):
        name, age = string.split(',')
        return cls(name, int(age))
    
    @staticmethod
    def is_adult(age):
        return age >= 18

# 继承
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade
    
    def study(self):
        return f"{self.name} is studying"

# 使用
person = Person('John', 25)
student = Student('Alice', 20, 'A')
```

### 私有属性和方法

```javascript
// JavaScript
class BankAccount {
    #balance = 0;  // 私有字段
    
    constructor(initialBalance) {
        this.#balance = initialBalance;
    }
    
    #validateAmount(amount) {  // 私有方法
        return amount > 0;
    }
    
    deposit(amount) {
        if (this.#validateAmount(amount)) {
            this.#balance += amount;
        }
    }
    
    getBalance() {
        return this.#balance;
    }
}
```

```python
# Python
class BankAccount:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # 私有属性（名称改写）
    
    def __validate_amount(self, amount):  # 私有方法
        return amount > 0
    
    def deposit(self, amount):
        if self.__validate_amount(amount):
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance
```

## 异步编程

### Promise/async-await vs asyncio

```javascript
// JavaScript
// Promise
function fetchData() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve('Data loaded');
        }, 1000);
    });
}

// async/await
async function loadData() {
    try {
        const data = await fetchData();
        console.log(data);
    } catch (error) {
        console.error(error);
    }
}

// 并行执行
async function loadMultipleData() {
    const [data1, data2] = await Promise.all([
        fetchData(),
        fetchData()
    ]);
}
```

```python
# Python
import asyncio

# 协程函数
async def fetch_data():
    await asyncio.sleep(1)  # 模拟异步操作
    return 'Data loaded'

# async/await
async def load_data():
    try:
        data = await fetch_data()
        print(data)
    except Exception as error:
        print(error)

# 并行执行
async def load_multiple_data():
    data1, data2 = await asyncio.gather(
        fetch_data(),
        fetch_data()
    )

# 运行异步函数
asyncio.run(load_data())
```

## 模块和导入

### 模块导入

```javascript
// JavaScript (ES6 模块)
// 导出 (math.js)
export const PI = 3.14159;
export function add(a, b) {
    return a + b;
}
export default function multiply(a, b) {
    return a * b;
}

// 导入 (main.js)
import multiply, { PI, add } from './math.js';
import * as math from './math.js';

// CommonJS (Node.js)
// 导出
module.exports = {
    PI: 3.14159,
    add: (a, b) => a + b
};

// 导入
const { PI, add } = require('./math');
```

```python
# Python
# 导出 (math_utils.py)
PI = 3.14159

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

# 导入 (main.py)
from math_utils import PI, add
import math_utils
from math_utils import *  # 导入所有（不推荐）

# 别名导入
import math_utils as math
from math_utils import add as addition
```

## 错误处理

```javascript
// JavaScript
try {
    let result = riskyOperation();
    console.log(result);
} catch (error) {
    console.error('Error:', error.message);
} finally {
    console.log('Cleanup');
}

// 抛出错误
function divide(a, b) {
    if (b === 0) {
        throw new Error('Division by zero');
    }
    return a / b;
}
```

```python
# Python
try:
    result = risky_operation()
    print(result)
except ValueError as e:
    print(f'Value Error: {e}')
except Exception as e:
    print(f'General Error: {e}')
else:
    print('No errors occurred')
finally:
    print('Cleanup')

# 抛出异常
def divide(a, b):
    if b == 0:
        raise ValueError('Division by zero')
    return a / b
```

## 常用内置方法

### 字符串操作

```javascript
// JavaScript
let str = 'Hello World';

str.length;                    // 11
str.toUpperCase();             // 'HELLO WORLD'
str.toLowerCase();             // 'hello world'
str.indexOf('World');          // 6
str.includes('Hello');         // true
str.split(' ');                // ['Hello', 'World']
str.replace('World', 'JS');    // 'Hello JS'
str.trim();                    // 去除首尾空格
str.substring(0, 5);           // 'Hello'
```

```python
# Python
string = 'Hello World'

len(string)                    # 11
string.upper()                 # 'HELLO WORLD'
string.lower()                 # 'hello world'
string.find('World')           # 6
'Hello' in string              # True
string.split(' ')              # ['Hello', 'World']
string.replace('World', 'Python')  # 'Hello Python'
string.strip()                 # 去除首尾空格
string[0:5]                    # 'Hello'
```

### 数组/列表操作

```javascript
// JavaScript
let arr = [1, 2, 3, 4, 5];

arr.length;                    // 5
arr.push(6);                   // 添加到末尾
arr.pop();                     // 删除末尾元素
arr.indexOf(3);                // 2
arr.includes(4);               // true
arr.join(', ');                // '1, 2, 3, 4, 5'

// 高阶函数
arr.map(x => x * 2);           // [2, 4, 6, 8, 10]
arr.filter(x => x > 2);        // [3, 4, 5]
arr.reduce((sum, x) => sum + x, 0);  // 15
arr.find(x => x > 3);          // 4
arr.some(x => x > 4);          // true
arr.every(x => x > 0);         // true
```

```python
# Python
list_val = [1, 2, 3, 4, 5]

len(list_val)                  # 5
list_val.append(6)             # 添加到末尾
list_val.pop()                 # 删除末尾元素
list_val.index(3)              # 2
4 in list_val                  # True
', '.join(map(str, list_val))  # '1, 2, 3, 4, 5'

# 列表推导式和内置函数
list(map(lambda x: x * 2, list_val))     # [2, 4, 6, 8, 10]
list(filter(lambda x: x > 2, list_val))  # [3, 4, 5]
sum(list_val)                            # 15
next(x for x in list_val if x > 3)       # 4
any(x > 4 for x in list_val)             # True
all(x > 0 for x in list_val)             # True
```

## 现代语法特性

### 解构赋值

```javascript
// JavaScript
// 数组解构
const [a, b, ...rest] = [1, 2, 3, 4, 5];
// a = 1, b = 2, rest = [3, 4, 5]

// 对象解构
const {name, age, ...others} = {name: 'John', age: 25, city: 'NY'};
// name = 'John', age = 25, others = {city: 'NY'}

// 函数参数解构
function greet({name, age}) {
    return `Hello ${name}, you are ${age}`;
}
```

```python
# Python
# 序列解构
a, b, *rest = [1, 2, 3, 4, 5]
# a = 1, b = 2, rest = [3, 4, 5]

# 字典解构（Python 3.5+）
data = {'name': 'John', 'age': 25, 'city': 'NY'}
name, age = data['name'], data['age']
# 或使用 ** 操作符
def greet(**kwargs):
    return f"Hello {kwargs['name']}, you are {kwargs['age']}"

greet(**data)
```

### 模板字符串/f-strings

```javascript
// JavaScript
const name = 'John';
const age = 25;

// 模板字符串
const message = `Hello ${name}, you are ${age} years old`;

// 多行字符串
const multiline = `
    This is a
    multiline string
`;
```

```python
# Python
name = 'John'
age = 25

# f-strings (Python 3.6+)
message = f"Hello {name}, you are {age} years old"

# 多行字符串
multiline = """
    This is a
    multiline string
"""

# 格式化表达式
value = 3.14159
formatted = f"Pi is approximately {value:.2f}"  # "Pi is approximately 3.14"
```

### 展开操作符/解包

```javascript
// JavaScript
// 数组展开
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2];  // [1, 2, 3, 4, 5, 6]

// 对象展开
const obj1 = {a: 1, b: 2};
const obj2 = {c: 3, d: 4};
const merged = {...obj1, ...obj2};    // {a: 1, b: 2, c: 3, d: 4}

// 函数调用
function sum(a, b, c) {
    return a + b + c;
}
sum(...arr1);  // 6
```

```python
# Python
# 列表解包
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = [*list1, *list2]  # [1, 2, 3, 4, 5, 6]

# 字典解包
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged = {**dict1, **dict2}  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 函数调用
def sum_numbers(a, b, c):
    return a + b + c

sum_numbers(*list1)  # 6
```

### 列表推导式/数组方法

```javascript
// JavaScript
const numbers = [1, 2, 3, 4, 5];

// 映射
const doubled = numbers.map(x => x * 2);

// 过滤
const evens = numbers.filter(x => x % 2 === 0);

// 组合操作
const result = numbers
    .filter(x => x > 2)
    .map(x => x * 2)
    .reduce((sum, x) => sum + x, 0);
```

```python
# Python
numbers = [1, 2, 3, 4, 5]

# 列表推导式
doubled = [x * 2 for x in numbers]

# 条件过滤
evens = [x for x in numbers if x % 2 == 0]

# 组合操作
result = sum(x * 2 for x in numbers if x > 2)

# 字典推导式
squares = {x: x**2 for x in numbers}

# 集合推导式
unique_evens = {x for x in numbers if x % 2 == 0}
```

## 🎯 实用技巧对比

### 交换变量

```javascript
// JavaScript
let a = 1, b = 2;
[a, b] = [b, a];  // ES6 解构
```

```python
# Python
a, b = 1, 2
a, b = b, a  # 直接交换
```

### 默认值处理

```javascript
// JavaScript
const value = input || 'default';  // 逻辑或
const value2 = input ?? 'default'; // 空值合并操作符
```

```python
# Python
value = input or 'default'  # 逻辑或
value2 = input if input is not None else 'default'  # 条件表达式
```

### 链式调用

```javascript
// JavaScript
const result = obj?.method?.()?.property;  // 可选链
```

```python
# Python
# 需要手动检查或使用 try-except
try:
    result = obj.method().property
except AttributeError:
    result = None
```

## 📚 学习建议

### 第一周：基础语法
1. 熟悉 Python 的缩进规则
2. 掌握基本数据类型和运算符
3. 练习条件语句和循环

### 第二周：数据结构和函数
1. 深入学习列表、字典、集合
2. 掌握函数定义和参数传递
3. 理解作用域和闭包

### 第三周：面向对象和模块
1. 学习类和继承
2. 了解模块和包的概念
3. 掌握异常处理

### 第四周：高级特性
1. 列表推导式和生成器
2. 装饰器和上下文管理器
3. 异步编程基础

## 🔗 相关资源

- [Python 官方文档](https://docs.python.org/3/)
- [Python 教程](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)
- [Python Tricks](https://realpython.com/python-tricks/)

## 💡 总结

通过这个对比指南，你应该能够：

1. **快速理解** Python 语法与 JavaScript 的相似性和差异
2. **利用已有知识** 加速 Python 学习过程
3. **避免常见陷阱** 如缩进、变量作用域等
4. **掌握核心概念** 为深入学习 Python 打下基础

记住，虽然语法不同，但编程的核心思想是相通的。你在 JavaScript 中学到的算法、设计模式和编程思维都可以直接应用到 Python 中！