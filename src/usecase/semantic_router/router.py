from semantic_router.encoders import OpenAIEncoder
from semantic_router import Route, RouteLayer
from semantic_router.utils.function_call import get_schema


def zupinnovation_balancesheet_documents(year: str):
    return f"Year: {year}"

def zupinnovation_employees(employee: dict, question: str):
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
        schema = get_schema(zupinnovation_balancesheet_documents)
        zupinnovation_employees_schema = get_schema(zupinnovation_employees)

        return RouteLayer(
            encoder=self.encoder, 
            routes=[
                Route(
                    name="zupinnovation_balancesheet_documents",
                    utterances=[
                        "zupinnovation_balancesheet_documents",
                        "balance sheet documents",
                        "documents",
                        "tools",
                        "zupinnovation_tools",
                        "metrics",
                    ],
                    function_schema=schema
                ), 
                Route(
                    name="zupinnovation_employees",
                    utterances=[
                        "employee business domain",
                        "paternity leave", 
                        'maternity leave',
                        "benefits",
                        "health insurance",
                        "vacation"
                    ],
                    function_schema=zupinnovation_employees_schema              
                )
            ]
        )
    
    def handler(self, request_body: str) -> str:        
        try:
            route = self._layer(request_body)            
            if route:
                if route.name == "zupinnovation_balancesheet_documents":                    
                    return "zupinnovation_balancesheet_documents"
                elif route.name == "zupinnovation_employees":                    
                    return "zupinnovation_employees"
                else:                
                    return "No tools are required"
            else:                
                return "Error: No route found."
        except Exception as e:            
            return str(e)