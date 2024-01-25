# Output MIME type
def print_MIMIE():
  import sys

  # Prompt User for file name and process it
  file= input("Pls type full file name: ").strip().lower()

  # Generate the MIME type
  media, extension = get_MIMIE(file)
  MIMIE=f"{media}/{extension}"
  print(MIMIE)
  sys.exit()



def get_MIMIE(file):
  """
function to generate the MIME type
"""
  
  # Extract the file extension
  extension = file.split(".")[-1]

  # Determine the MIME type based on the file extension
  match extension:
     case "gif"|"png":
       return ["image",extension]
     case "jpeg"|"jpg":
       return ["image","jpeg"]
     case "pdf":
       return ["application",extension]
     case "text":
       return ["text","plain"]
     case "zip":
       return ["application",extension]
     case _:
       return ["application","octet-stream"]

print_MIMIE()