#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import JsonResponse
from opsssh.utils import tools
import json

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')

    elif request.method == 'POST':
        success = {'code': 0, 'message': None, 'error': None}
        try:
            post_data = request.POST.get('data')
            data = json.loads(post_data)
            print(data)
            auth = data.get('auth')
            if auth == 'key':
                pkey = request.FILES.get('pkey')
                key_content = pkey.read().decode('utf-8')
                data['pkey'] = key_content
            else:
                data['password'] = data.get('password')

            unique = tools.unique()
            data['unique'] = unique

            valid_data = tools.ValidationData(data)

            if valid_data.is_valid():
                valid_data.save()
                success['message'] = unique
            else:
                error_json = valid_data.errors.as_json()
                success['code'] = 1
                success['error'] = error_json

            return JsonResponse(success)
        except Exception as error:
            print(error)
            success['code'] = 1
            success['error'] = error
            return JsonResponse(success)
