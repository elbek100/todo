from django.shortcuts import render, redirect
from django.views import View

from main.models import Service


class HomeTemplateView(View):
          templates_name = 'Home.html'
          context = {}

          def get(self,request):
              service = Service.objects.all(owner_id = request.user)
              self.context.update(service)
              return render(request, self.templates_name , self.context)


class TodoTemplateView(View):
    templates_name = 'todo.html'
    context = {}

    def get(self, request):
        return render(request, self.templates_name, self.context)

    def post(self, request):
        text = request.POST.get('text')
        user_id = request.user.id

        if user_id is not None:
            service = Service.objects.create(
                text=text,
                owner_id=user_id
            )
            service.save()
            return redirect('/todo')
        else :
            return redirect('/accounts/login')
