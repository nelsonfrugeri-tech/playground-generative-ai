from semantic_router.encoders import OpenAIEncoder
from semantic_router import Route, RouteLayer
from semantic_router.utils.function_call import get_schema


def balancesheet_documents(year: str):
    return f"Year: {year}"

def employees(employee: dict, question: str):
    """
    employee: information about the employee
    question: employee questions
    """
    return "Employees"


class Router:
    def __init__(self):
        self.encoder = OpenAIEncoder("text-embedding-ada-002")
        self._layer = self._route_layer()

    def _route_layer(self):
        schema = get_schema(balancesheet_documents)
        employees_schema = get_schema(employees)

        return RouteLayer(
            encoder=self.encoder, 
            routes=[
                Route(
                    name="balancesheet_documents",
                    utterances=[
                        "balancesheet_documents",
                        "balance sheet documents",
                        "documents",
                        "tools",
                        "tools",
                        "metrics",
                    ],
                    function_schema=schema
                ), 
                Route(
                    name="employees",
                    utterances=[
                        "employee business domain",
                        "paternity leave", 
                        'maternity leave',
                        "benefits",
                        "health insurance",
                        "vacation"
                    ],
                    function_schema=employees_schema              
                )
            ]
        )
    
    def handler(self, request_body: str) -> str:        
        try:
            route = self._layer(request_body)            
            if route:
                if route.name == "balancesheet_documents":                    
                    return "balancesheet_documents"
                elif route.name == "employees":                    
                    return "employees"
                else:                
                    return "No tools are required"
            else:                
                return "Error: No route found."
        except Exception as e:            
            return str(e)