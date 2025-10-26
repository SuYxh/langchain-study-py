from utils import sum_numbers, sum_list, average, multiply_numbers


def main():
    print("Hello from langchain-study-py!")
    print("\n=== 使用工具函数演示 ===")
    
    # 使用求和函数
    result1 = sum_numbers(10, 20, 30, 40, 50)
    print(f"sum_numbers(10, 20, 30, 40, 50) = {result1}")
    
    # 使用列表求和
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result2 = sum_list(numbers)
    print(f"sum_list({numbers}) = {result2}")
    
    # 计算平均值
    avg = average(numbers)
    print(f"average({numbers}) = {avg}")
    
    # 计算乘积
    result3 = multiply_numbers(2, 3, 4, 5)
    print(f"multiply_numbers(2, 3, 4, 5) = {result3}")
    
    # 演示浮点数计算
    float_result = sum_numbers(1.5, 2.5, 3.7, 4.3)
    print(f"sum_numbers(1.5, 2.5, 3.7, 4.3) = {float_result}")
    
    print("\n✅ 所有计算完成！")


if __name__ == "__main__":
    main()
