"""工具函数模块

包含各种实用的工具函数，如数学计算、字符串处理等。
"""

from typing import List, Union


def sum_numbers(*args: Union[int, float]) -> Union[int, float]:
    """计算多个数字的和
    
    Args:
        *args: 可变数量的数字参数
        
    Returns:
        所有数字的和
        
    Examples:
        >>> sum_numbers(1, 2, 3)
        6
        >>> sum_numbers(1.5, 2.5, 3.0)
        7.0
    """
    return sum(args)


def sum_list(numbers: List[Union[int, float]]) -> Union[int, float]:
    """计算列表中所有数字的和
    
    Args:
        numbers: 包含数字的列表
        
    Returns:
        列表中所有数字的和
        
    Examples:
        >>> sum_list([1, 2, 3, 4, 5])
        15
        >>> sum_list([1.1, 2.2, 3.3])
        6.6
    """
    return sum(numbers)


def average(numbers: List[Union[int, float]]) -> float:
    """计算数字列表的平均值
    
    Args:
        numbers: 包含数字的列表
        
    Returns:
        平均值
        
    Raises:
        ValueError: 当列表为空时
        
    Examples:
        >>> average([1, 2, 3, 4, 5])
        3.0
        >>> average([10, 20, 30])
        20.0
    """
    if not numbers:
        raise ValueError("列表不能为空")
    
    return sum(numbers) / len(numbers)


def multiply_numbers(*args: Union[int, float]) -> Union[int, float]:
    """计算多个数字的乘积
    
    Args:
        *args: 可变数量的数字参数
        
    Returns:
        所有数字的乘积
        
    Examples:
        >>> multiply_numbers(2, 3, 4)
        24
        >>> multiply_numbers(1.5, 2, 3)
        9.0
    """
    if not args:
        return 0
    
    result = 1
    for num in args:
        result *= num
    return result


def main():
    """演示工具函数的使用"""
    print("=== 工具函数演示 ===")
    
    # 测试求和函数
    print(f"sum_numbers(1, 2, 3, 4, 5) = {sum_numbers(1, 2, 3, 4, 5)}")
    print(f"sum_numbers(1.5, 2.5, 3.0) = {sum_numbers(1.5, 2.5, 3.0)}")
    
    # 测试列表求和
    numbers = [10, 20, 30, 40, 50]
    print(f"sum_list({numbers}) = {sum_list(numbers)}")
    
    # 测试平均值
    print(f"average({numbers}) = {average(numbers)}")
    
    # 测试乘积
    print(f"multiply_numbers(2, 3, 4) = {multiply_numbers(2, 3, 4)}")
    print(f"multiply_numbers(1.5, 2, 3) = {multiply_numbers(1.5, 2, 3)}")


if __name__ == "__main__":
    main()