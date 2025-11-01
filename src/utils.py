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


def parse_agent_response(response: dict) -> dict:
    """解析Agent响应信息
    
    Args:
        response: Agent的响应字典，包含messages列表
        
    Returns:
        包含解析结果的字典，包括:
        - total_input_tokens: 总输入token数
        - total_output_tokens: 总输出token数  
        - total_tokens: 总token数
        - ai_final_response: AI最终回复内容
        - tool_results: 工具调用结果列表
        - conversation_flow: 对话流程详情
    """
    messages = response['messages']
    
    # 初始化统计变量
    total_input_tokens = 0
    total_output_tokens = 0
    total_tokens = 0
    ai_final_response = ""
    tool_results = []
    conversation_flow = []
    
    # 解析每个消息
    for i, message in enumerate(messages, 1):
        message_type = str(message.__class__.__name__)
        message_info = {"step": i, "type": message_type}
        
        if message_type == "HumanMessage":
            message_info["content"] = f"用户问题: {message.content}"
        
        elif message_type == "AIMessage":
            if hasattr(message, 'tool_calls') and message.tool_calls:
                tool_names = [tool['name'] for tool in message.tool_calls]
                message_info["content"] = f"AI决定调用工具: {tool_names}"
                if message.content:
                    message_info["ai_content"] = message.content
            else:
                message_info["content"] = f"AI回复: {message.content}"
                ai_final_response = message.content
        
        elif message_type == "ToolMessage":
            message_info["content"] = f"工具名称: {message.name}"
            message_info["tool_result"] = f"工具结果: {message.content}"
            tool_results.append({"name": message.name, "result": message.content})
        
        # 提取token使用信息
        if hasattr(message, 'usage_metadata') and message.usage_metadata:
            tokens = message.usage_metadata
            input_tokens = tokens.get('input_tokens', 0)
            output_tokens = tokens.get('output_tokens', 0)
            total_msg_tokens = tokens.get('total_tokens', 0)
            
            message_info["tokens"] = {
                "input": input_tokens,
                "output": output_tokens, 
                "total": total_msg_tokens
            }
            
            total_input_tokens += input_tokens
            total_output_tokens += output_tokens
            total_tokens += total_msg_tokens
        
        conversation_flow.append(message_info)
    
    return {
        "total_input_tokens": total_input_tokens,
        "total_output_tokens": total_output_tokens,
        "total_tokens": total_tokens,
        "ai_final_response": ai_final_response,
        "tool_results": tool_results,
        "conversation_flow": conversation_flow
    }


def print_agent_response_analysis(response: dict, 
                                 show_conversation_flow: bool = False,
                                 show_token_usage: bool = False, 
                                 show_tool_results: bool = False,
                                 show_summary: bool = False) -> None:
    """打印Agent响应分析结果
    
    Args:
        response: Agent的响应字典
        show_conversation_flow: 是否显示对话流程详情，默认False
        show_token_usage: 是否显示token消耗信息，默认False
        show_tool_results: 是否显示工具调用结果，默认False
        show_summary: 是否显示汇总信息，默认False
    """
    analysis = parse_agent_response(response)
    
    # 默认只输出AI最终回复
    if not any([show_conversation_flow, show_token_usage, show_tool_results, show_summary]):
        print(analysis['ai_final_response'])
        return
    
    # 显示对话流程详情
    if show_conversation_flow:
        print(f"\n=== 对话流程详情 ===")
        for flow in analysis["conversation_flow"]:
            print(f"\n{flow['step']}. {flow['type']}:")
            print(f"   {flow['content']}")
            
            if "ai_content" in flow:
                print(f"   AI内容: {flow['ai_content']}")
            if "tool_result" in flow:
                print(f"   {flow['tool_result']}")
            if show_token_usage and "tokens" in flow:
                tokens = flow["tokens"]
                print(f"   Token消耗: 输入={tokens['input']}, 输出={tokens['output']}, 总计={tokens['total']}")
    
    # 显示汇总信息
    if show_summary:
        print(f"\n=== 汇总信息 ===")
        if show_token_usage:
            print(f"总Token消耗: 输入={analysis['total_input_tokens']}, 输出={analysis['total_output_tokens']}, 总计={analysis['total_tokens']}")
        
        if show_tool_results and analysis["tool_results"]:
            print(f"\n工具调用结果:")
            for tool in analysis["tool_results"]:
                print(f"  - {tool['name']}: {tool['result']}")
    
    # 显示AI最终回复
    print(f"\nAI最终回复: {analysis['ai_final_response']}")


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
