import http
from os import access
from unicodedata import name
from urllib import request
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.generic import View
import requests
import json
from .models import Users_kakao


# Create your views here.

kakao_login = {
    "restapi_key": "8b2b5ab728f803945cc2f0c29a1aa84b",
    "redirect_uri": "http://localhost:8000/oauth/callback/",
    "client_secret_key": "LewDjbXzmoSsznVNq2bycROMlxwsHFYi",
}

kakao_login_uri = "https://kauth.kakao.com/oauth/authorize?response_type=code"
kakao_token_uri = "https://kauth.kakao.com/oauth/token"
kakao_profile_uri = "https://kapi.kakao.com/v2/user/me"

def start(request):
    template = loader.get_template('managements/start.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

class Kakaoview(View):
    def get(self, request):
        kakao_api = "https://kauth.kakao.com/oauth/authorize?response_type=code"
        redirect_uri = "http://localhost:8000/oauth/callback/"
        app_key = "8b2b5ab728f803945cc2f0c29a1aa84b"
        
        return redirect(f"{kakao_api}&client_id={app_key}&redirect_uri={redirect_uri}")
    
class Kakaocallback(View):
    def get(self, request):
        request_data = {
            "grant_type": "authorization_code",
            "client_id": "8b2b5ab728f803945cc2f0c29a1aa84b",
            "redirect_uri": "http://localhost:8000/oauth/callback/",
            "code": request.GET["code"]
        }
        
        kakao_token_api = "https://kauth.kakao.com/oauth/token"
        token_headers = {
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }
        token_res = requests.post(kakao_token_api, data=request_data, headers=token_headers)
        
        token_json = token_res.json()

        access_token =  token_json.get("access_token")
        
        auth_headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        user_info_response = requests.get("https://kapi.kakao.com/v2/user/me", headers=auth_headers)
        user_info_json = user_info_response.json()
        kakao_account = user_info_json.get('kakao_account')
        if not kakao_account:
            return HttpResponse("시발")
        user_id = user_info_json.get('id')
        if Users_kakao.objects.filter(user_id=user_id):
            return redirect(f"/managements/")
        else:
            user_name = kakao_account.get("profile")["nickname"]
            user_proflie = kakao_account.get("profile")["thumbnail_image_url"]
            Users_kakao.objects.create(name=user_name, profile=user_proflie, user_id=user_id)
            return redirect(f"/managements/")
    
def log_out(request):
    app_key = "8b2b5ab728f803945cc2f0c29a1aa84b"
    redirect_uri = "http://localhost:8000/"
    kakao_service_logout_url = "https://kauth.kakao.com/oauth/logout"
    return redirect(f"{kakao_service_logout_url}?client_id={app_key}&logout_redirect_uri={redirect_uri}")
    
    
def management(request):
    template = loader.get_template('managements/management.html')
    context = {

    }
    return HttpResponse(template.render(context, request))