import requests

class fip_app_iterator:
    def __init__(self, brand_id):
        self.brand_id = brand_id
        self.page = 1
        self.has_next_page = True
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.has_next_page:
            raise StopIteration
        
        url = f"https://parallelum.com.br/fipe/api/v1/carros/marcas?page={self.page}"
    
        response = requests.get(url)
        
        if response.status_code == 200:
        
            data = response.json()
        
            cars = data.get('cars', [])
        
            self.page += 1
        
            self.has_next_page = bool(cars)
        
            return cars
        else:
            
            raise Exception(f"falha ao obter dados da API.codigo status {response.status_code}")