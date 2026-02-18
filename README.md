# app-stocks

> [!NOTE]
> For most of my projects, the leading branch is the **dev** one. That means that *_dev.yaml file is the most frequently used workflow/pipeline.  

Simple app for retrive the stock exchange data.  

Tools:
- Azure Static Web App
- backend: Azure Function v2 API (Python) emulated in SWA
- frontend: JS, HTML/CSS
- Single Page App (SPA) ?

Issues:
- Failed to containerized Azure Function (no Selenium): ```--kind functionapp```
- Failed to use yfinance API in Azure Function: ```Language Worker Process (Python) exited```
- SWA Azure Function v2 API emulation crash on this line: ```f"Failed to retrieved {symbol} stock data: {response.json()["code"]}"```  

API support in Azure Static Web Apps with Azure Functions restrictions:
- Managed functions: By default, the API of a static web app is an Azure Functions application managed and deployed by Azure Static Web Apps associated with some restrictions
- supported Azure Function hosting plans: Consumption ?
- The Azure Functions app must either be in Python 3.8, Python 3.9, or Python 3.10  

<br>

> [!NOTE]
>To distinguish between local and remote environment, use a system variable, for example AZURE_ENVIRONMENT:    
>```az staticwebapp appsettings set -g "${{ ... }}" -n "${{ ... }}" --setting-names AZURE_ENVIRONMENT="${{ secrets.AZURE_ENVIRONMENT }}"```  
>then in the code, ```os.getenv("AZURE_ENVIRONMENT", "local")```  

<br>

> [!NOTE]
>Local environment variables:  
>- Powershell/Bash script  
>- **.env** File: Best for project-specific secrets shared with other developers (usually requires dotenv package in code)  
>- **terminal.integrated.env.windows (terminal.integrated.env.linux)**: Best for local development environment machine-specific paths or variables, could be combined with **.env** file  


### Set environment variables via Powershell code (Windows 11):
Temporary in a current Powershell session:  
```$env:VARIABLE_NAME = "Value"```

Permanently in privilege mode:  
```[Environment]::SetEnvironmentVariable('MyVariable', 'Some value', 'Machine')```

Broadcast change to Windows:  
```$env:MyVariable = [System.Environment]::GetEnvironmentVariable('MyVariable', 'Machine')```

Remove system variable:  
```Remove-Item Env:MyVariable```

Display system variables via Powershell:  
```Get-ChildItem Env:```

### Set environment variables via VSC terminal.integrated.env.windows (or terminal.integrated.env.linux):
File -> Preferences -> Settings  
Find @id:terminal.integrated.env.windows  
Select which config you would like to change - User’s or Worspace (recommended)  
For the setting Terminal › Integrated › Env: Windows, click the **Edit in settings.json** link  
Define your environment variables here:  
```
{
    "terminal.integrated.env.windows": {
        "MY_VARIABLE1": "",
        "MY_VARIABLE2": ""
    }
}
```  
or point to .env file:  
```
{
    "terminal.integrated.env.windows": {
        "PATH": ".env"
    }
}
```  

<br>

Configure Azure Static Web App:  
https://learn.microsoft.com/en-us/azure/static-web-apps/configuration#platform  
API support in Azure Static Web Apps with Azure Functions:  
https://learn.microsoft.com/en-us/azure/static-web-apps/apis-functions?source=recommendations  
Build configuration for Azure Static Web Apps:  
https://learn.microsoft.com/en-us/azure/static-web-apps/build-configuration?tabs=identity&pivots=github-actions  
Build your Python Azure Functions apps:  
https://learn.microsoft.com/en-us/azure/azure-functions/python-build-options  

<br>

Static Web App (locally):  
https://azure.github.io/static-web-apps-cli/docs/use/install  
swa start src --api-location api  
<!-- npx @azure/static-web-apps-cli start --api-location /api   -->
