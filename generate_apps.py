import os
import re
import subprocess

SETTINGS_PATH = os.path.join("config", "settings.py")

with open(SETTINGS_PATH, "r") as f:
    content = f.read()

pattern = r"'(my_[a-zA-Z0-9_]+)'"
apps = re.findall(pattern, content)

for app in apps:
    if not os.path.exists(app):
        print(f"Creating app: {app}")
        subprocess.run(["python", "manage.py", "startapp", app])
    else:
        print(f"App already exists: {app}")
        
import os
import re
import subprocess

SETTINGS_PATH = os.path.join("config", "settings.py")
URLS_PATH = os.path.join("config", "urls.py")

# Step 1: Extract custom apps from settings.py
with open(SETTINGS_PATH, "r") as f:
    content = f.read()

pattern = r"'(my_[a-zA-Z0-9_]+)'"
apps = re.findall(pattern, content)

# Step 2: Create apps and add urls.py if missing
for app in apps:
    if not os.path.exists(app):
        print(f"Creating app: {app}")
        subprocess.run(["python", "manage.py", "startapp", app])
    else:
        print(f"App already exists: {app}")

    urls_file = os.path.join(app, "urls.py")
    if not os.path.exists(urls_file):
        with open(urls_file, "w") as f:
            f.write(f"""from django.urls import path

urlpatterns = [
    # path('', views.index, name='{app}_index'),
]
""")
        print(f"Created {urls_file}")

# Step 3: Inject includes into config/urls.py
with open(URLS_PATH, "r") as f:
    urls_content = f.read()

for app in apps:
    include_line = f"path('{app}/', include('{app}.urls')),"
    if include_line not in urls_content:
        # Add import if missing
        if "from django.urls import path, include" not in urls_content:
            urls_content = urls_content.replace(
                "from django.urls import path",
                "from django.urls import path, include"
            )
        # Add the include line
        urls_content = urls_content.replace(
            "urlpatterns = [",
            f"urlpatterns = [\n    {include_line}"
        )

with open(URLS_PATH, "w") as f:
    f.write(urls_content)

print("✅ All apps scaffolded and URLs wired up!")

import os
import re
import subprocess

SETTINGS_PATH = os.path.join("config", "settings.py")
URLS_PATH = os.path.join("config", "urls.py")

with open(SETTINGS_PATH, "r") as f:
    content = f.read()

pattern = r"'(my_[a-zA-Z0-9_]+)'"
apps = re.findall(pattern, content)

for app in apps:
    if not os.path.exists(app):
        print(f"Creating app: {app}")
        subprocess.run(["python", "manage.py", "startapp", app])
    else:
        print(f"App already exists: {app}")

    # Create views.py with index view
    views_path = os.path.join(app, "views.py")
    with open(views_path, "w") as f:
        f.write(f"""from django.shortcuts import render

def index(request):
    return render(request, '{app}/index.html')
""")

    # Create urls.py
    urls_path = os.path.join(app, "urls.py")
    with open(urls_path, "w") as f:
        f.write(f"""from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='{app}_index'),
]
""")

    # Create template directory and index.html
    template_dir = os.path.join(app, "templates", app)
    os.makedirs(template_dir, exist_ok=True)
    with open(os.path.join(template_dir, "index.html"), "w") as f:
        f.write(f"<h1>Welcome to {app.replace('_', ' ').title()}</h1>")

# Inject includes into config/urls.py
with open(URLS_PATH, "r") as f:
    urls_content = f.read()

for app in apps:
    include_line = f"path('{app}/', include('{app}.urls')),"
    if include_line not in urls_content:
        if "from django.urls import path, include" not in urls_content:
            urls_content = urls_content.replace(
                "from django.urls import path",
                "from django.urls import path, include"
            )
        urls_content = urls_content.replace(
            "urlpatterns = [",
            f"urlpatterns = [\n    {include_line}"
        )

with open(URLS_PATH, "w") as f:
    f.write(urls_content)

print("✅ All apps scaffolded with views, templates, and routing!")