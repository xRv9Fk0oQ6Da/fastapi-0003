# fastapi-0003

If anyone is having issues setting up Python FastAPI with Gcloud or Heroku, 
you may use this as a base-line example, with a registration/login and JWT 
return token. 
---
### **The Reasons why I was having issues is because:**
1) Gcloud was a way to complex for a simple Python API. 
  >They started charging before the API was even established.

2) Heroku hosts apps for free; and won't (or shouldn't) cap the API like Gcloud.
  >Longer life-cycle acceptance for hobbiests. 

3) When setting up the API I had to link a Github Repo (create one) to the 
  >Heroku app (create a new one) then save, commit and push your edits to your Git Repo.

4) Conflicting plugins; JWT and PyJWT can not both exist at the same time; use PyJWT
  >That way you can get Tokens
---
Remember, Select ***BuildPack***: ***heroku/python***
- [x] Settings -> Add buildpack -> heroku/python
---
Congrats, you got a live Python FastAPI and hopefully it was a lot less stressful than it 
was for me learning it on my own at home without any helpful resources online.

If this has helped you, please give me a star. 

Good luck!
