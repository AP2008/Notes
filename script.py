"MODULE"
import os
import subprocess

HTML_TEMPLATE = """
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="https://bootswatch.com/5/lux/bootstrap.min.css">
  <style>
    .background-img {{
        inset: 0px;
        transition: opacity 0.1s ease 0s;
        z-index: -1;
        background-position: center center;
        background-size: cover;
    }}
  </style>
</head>
<body style="overflow-x: hidden;" class="container-fluid">
  <center><h1>My NOTES</h1></center>
  <div class="row">
  {}
  </div>
</body>
"""

CARD_TEMPLATE = """
    <div class="column col-md-4">
      <div class="card">
        <div>
          <div class="background-img" style="background-image: linear-gradient(rgba(255,255,255,.5), rgba(255,255,255,.5)), url({icon})">
            <div style="padding-left: 18px; padding-top: 18px; padding-bottom: 18px; padding-right: 18px;">
              <h3 style="text-transform: capitalize;">{title}</h3>
            </div>
          </div>
        </div>
        <div class="card-body">
          <p class="card-text">{content}</p>
          <a href="{pdf}" class="btn btn-primary">Download</a>
        </div>
      </div>
    </div>
"""

CARDS = ""

dirs = list(filter(lambda x: x[0] != ".", os.listdir("../")))
dirs.remove("www")

for dirName in dirs:
    dirFiles = os.listdir(f"../{dirName}")
    for file in dirFiles:
        if file[:4] == "icon":
            icon = file
            break
    subprocess.run(["cp", f"../{dirName}/{dirName}.pdf", "./pdfs/"])
    subprocess.run(["cp", f"../{dirName}/{icon}", f"./icons/{dirName}-{icon}"])
    CARDS += CARD_TEMPLATE.format(
        icon=f"./icons/{dirName}-{icon}",
        pdf=f"./pdfs/{dirName}.pdf",
        content=open(f"../{dirName}/{dirName}.text").read().replace("\n\n", "<br>").replace("\n", "")[:300],
        title=f"{dirName}".replace("_", " ")
    )
open("index.html", "w+").write(HTML_TEMPLATE.format(CARDS))
