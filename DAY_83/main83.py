# This is Day 83 project : Simple CMS (Content Management System)

import json
from content import ContentManager
from storage import ContentStorage

def show(action, result, status=200):
    print(f"\nREQUEST {action}\nRESPONSE {status}\n{json.dumps(result, indent=2)}")
    
def main():
    print("Day 83 - Simple CMS (Content Management System)")
    cms = ContentManager(ContentStorage())
    page = cms.create("About Us", "about-us", "We build useful software.")
    show("CREATE PAGE", page.to_dict(), 201)
    show("PUBLISH PAGE", cms.publish(page.id).to_dict())
    show("LIST PUBLISHED", {"pages": [p.to_dict() for p in cms.published()]})
    
if __name__ == "__main__":
    main()
    
# Done