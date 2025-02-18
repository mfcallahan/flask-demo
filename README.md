# Flask Demo App

This repository contains a sample Python Flask application which can also import the ArcPy and ArcGIS Pro Python API packages from Esri.

## Configure your machine to run this app locally

- If a cloned ArcGIS Pro Python environment does not exist on you local development machine, clone the default "arcgispro-py3" environment from the ArcGIS Pro Package Manager.
- From the command line, navigate to the "Scripts" folder within the ArcGIS Pro installation folder, typically one of these locations:
    - %LocalAppData%\Programs\ArcGIS\Pro\bin\Python\Scripts
    - %ProgramFiles%\ArcGIS\Pro\bin\Python\Scripts
    - `cd %LocalAppData%\Programs\ArcGIS\Pro\bin\Python\Scripts`
- Execute the "proenv.bat" file in the command line to activate the ArcGIS Pro Conda environment.
- From the command line, navigate to the folder containing your cloned ArcGIS Pro Python environment, typically one of these locations:
    - %LocalAppData%\ESRI\conda\envs
    - %ProgramFiles%\ArcGIS\Pro\bin\Python\envs
    - `cd %LocalAppData%\ESRI\conda\envs`
- Activate your cloned ArcGIS Pro Python environment, using the name of your cloned environment:
    - `activate arcgispro-py3-clone`
- With your cloned environment activated, install these dependencies:
    - `conda install flask`
    - `conda install wfastcgi`
- Copy file "wfastcgi.py" to the root app folder (/flask-demo) from the Python site-packages folder, typically in one of these locations:
    - %LocalAppData%\ESRI\conda\envs\arcgispro-py3-clone\Lib\site-packages\wfastcgi.py
    - %ProgramFiles%\ArcGIS\Pro\bin\Python\envs\arcgispro-py3-clone\Lib\site-packages\site-packages\wfastcgi.py
- In your development environment, set the Python interpreter path to the "python.exe" file found in your cloned ArcGIS Pro Python environment folder.
    - If using VS Code, this can be done by opening the command pallette (Ctrl + Shift + P) and searching for "Python: Select interpreter" > Enter interpreter path > Find... > navigate to your cloned ArcGIS Pro Python environment folder and select the "python.exe" file.
- With the cloned Python environment still activated, change the directory to this app's root folder:
    - `cd C:\path\to\tools\Templates\Flask\flask-demo
- Set a "FLASK_APP" environmet variable:
    - `set FLASK_APP=app.py`
- Start the Flask development server:
    - `python -m flask run`
- The app server will be running on  http://localhost:5000/ and this app will be available on http://localhost:5000/flask-demo/

## Deploying to IIS

- Connect to your Windows Server machine
- Copy app code to C:\inetpub\wwwroot\flask-demo\
- Clone the default "arcgispro-py3" environment from the ArcGIS Pro Package Manager. The location of the clonsed environment must be in the app folder: C:\inetpub\wwwroot\flask-demo\arcgispro-py3-flask-demo
- From the command line, navigate to the "Scripts" folder within the ArcGIS Pro installation folder:
    - `cd %ProgramFiles%\ArcGIS\Pro\bin\Python\Scripts`
- Execute the "proenv.bat" file in the command line to activate the ArcGIS Pro Conda environment.
- From the command line, navigate to the folder containing your cloned ArcGIS Pro Python environment:
    - `cd C:\inetpub\wwwroot\flask-demo\arcgispro-py3-flask-demo`
- Activate your cloned ArcGIS Pro Python environment, using the name of your cloned environment:
    - `activate arcgispro-py3-flask-demo`
- With your cloned environment activated, install these dependencies:
    - `conda install flask`
    - `conda install wfastcgi`
- Copy file "wfastcgi.py" to the root app folder (/flask-demo) from the Python site-packages folder:
    - %ProgramFiles%\ArcGIS\Pro\bin\Python\envs\arcgispro-py3-flask-demo\Lib\site-packages\site-packages\wfastcgi.py
- Create a new application pool
    - Name: flask-demo
    - .NET CLR Version: No managed code
    - Managed pipeline mode: Integrated
    - Under the app pool's Advanced Settings, set Process Model > Identity to your account name 
- Convert the folder to an application
    - website > flask-demo > right click > Convert to application
        - Set Alias as "flask-demo"
        - Set physical path as newly created app folder `C:\inetpub\wwwroot\flask-demo\`
        - Application pool: flask-demo
- Set app folder ownership:
    - Right click app folder `C:\inetpub\wwwroot\flask-demo\` and select Properties > Security > Advanced
    - Set location as the current machine name
    - Change owner to "IIS AppPool\flask-demo"
    - Check "Replace all child object permissions..."
    - Click OK
- Update the web.config file and add the following inside `<configuration> <system.webServer> <handlers>`:
    - `<add name="Python FastCGI" path="*" verb="*" modules="FastCgiModule" scriptProcessor="C:\inetpub\wwwroot\flask-demo\arcgispro-py3-flask-demo\python.exe|C:\inetpub\wwwroot\flask-demo\wfastcgi.py" resourceType="Unspecified" requireAccess="Script" />`
- Add app to FastCGI Server Settings:
    - IIS > Server Name > FastCGI Settings > Add Application:
    - Full path: `C:\inetpub\wwwroot\flask-demo\arcgispro-py3-flask-demo\python.exe`
    - Arguments: `C:\inetpub\wwwroot\flask-demo\wfastcgi.py`

## See also:

[Flask Tutorial in Visual Studio Code](https://code.visualstudio.com/docs/python/tutorial-flask)
