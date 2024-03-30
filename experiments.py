import mlflow

def calculator(a,b,operation=None):
    if operation == "add":
        return (a + b)

    if operation == "sub":
        return (a - b)

    if operation == "mul":
        return (a * b)
    
    if operation == "div":
        return (a / b)

if __name__ == "__main__":
    a,b,operation = 10,20,"mul"
    with mlflow.start_run():
        result = calculator(a,b,operation)
        mlflow.log_param("a",a)
        mlflow.log_param("b",b)
        mlflow.log_param("operation",operation)
        print(f"my result regarding the {operation} is {result}")
        mlflow.log_param("result",result)

