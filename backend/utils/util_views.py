from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView, status

from utils.retry_session import get_retry_session
from utils.utils import is_process_running, log_file_reader


class PingAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, requset: Request):
        scraping_process_status = is_process_running("scraping.py")
        messaging_process_status = is_process_running("messaging.py")
        res = dict(
            scraping_process_statu=scraping_process_status,
            messaging_process_status=messaging_process_status,
        )
        return Response(status=status.HTTP_200_OK, data=res)


@login_required
def log_view(request):
    scraping_log_file_path = (
        "/root/tenplestay/backend/worker/logs/tenplestay-scraping-worker.log"
    )
    messaging_log_file_path = (
        "/root/tenplestay/backend/worker/logs/tenplestay-messaging-worker.log"
    )

    return render(
        request,
        "log_template.html",
        {
            "scraping_log_content": log_file_reader(scraping_log_file_path),
            "messaging_log_content": log_file_reader(messaging_log_file_path),
        },
    )


class NClovaStudioApp:
    """
    ### 네이버 클로바 스튜디오 API
    - https://clovastudio.ncloud.com/explorer/tools/summarization/v2
    - 길고 복잡한 문장을 간략하게 요약합니다.
    """

    def __init__(self) -> None:
        self.url = "https://clovastudio.apigw.ntruss.com/testapp/v1/api-tools/summarization/v2/6875a176076a4c9da483f57c4cf82575"
        self.headers = {
            "X-NCP-CLOVASTUDIO-API-KEY": settings.X_NCP_CLOVASTUDIO_API_KEY,
            "X-NCP-APIGW-API-KEY": settings.X_NCP_APIGW_API_KEY,
            "X-NCP-CLOVASTUDIO-REQUEST-ID": settings.X_NCP_CLOVASTUDIO_REQUEST_ID,
            "Content-Type": "application/json",
        }

    def set_payload(self, text: str) -> dict:
        return {
            "texts": [text],
            "segMinSize": 300,
            "includeAiFilters": True,
            "maxTokens": 256,
            "autoSentenceSplitter": True,
            "segCount": -1,
            "segMaxSize": 1000,
        }

    def get_summarization(self, text: str) -> dict:
        if not text:
            raise Exception("요약하기 위한 문자열로 빈 문자열이 올 수 없습니다.")

        s = get_retry_session()
        res = s.post(self.url, json=self.set_payload(text), headers=self.headers).json()
        return res["result"]
