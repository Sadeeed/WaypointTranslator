from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.http import FileResponse

from converter.converter import convert_to_xaero
from converter.forms import UploadFileForm


class VoxelMapToXaeroConverterView(FormView):
    form_class = UploadFileForm
    template_name = 'document.html'
    success_url = '/'
    # success_message = 'Conversion Complete :)'

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            # messages.error(self.request, self.success_message)
            # waypoint_obj = form.save()
            # converted_waypoints, filepath = convert_to_xaero(request.FILES['file'])
            waypoint_file = request.FILES['file']
            try:
                converted_waypoints = convert_to_xaero(waypoint_file)
                print(converted_waypoints)
                # return self.form_valid(form)
                # return HttpResponse(converted_waypoints, content_type='text/plain')
                return JsonResponse({'converted_waypoints': converted_waypoints}, status=200)
            except Exception as e:
                print("Error: ", e)
                return JsonResponse({'error': 'We are facing some issues please try again'}, status=400)
            # return FileResponse(open(filepath, 'rb'), as_attachment=True)
            # return render(request, 'output.html', {'converted_waypoints': converted_waypoints})
        else:
            # return self.form_invalid(form)
            return JsonResponse({'error': 'Invalid file, please try again'}, status=400)


class DownloadFileView(TemplateView):
    template_name = 'output.html'


class InstructionsView(TemplateView):
    template_name = 'instructions.html'
