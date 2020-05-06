def get_ko_sub(video_url):
    """
    동영상 url을 매개변수로 받아 한국어 자막이 있는지 확인하고
    있으면 한국어 자막을, 존재하지 않으면 'Korean Sub does not exist'를
    리턴합니다.
    """
      from pytube import YouTube
      
      yt = YouTube(video_url)
      all_caption = yt.captions.all() # 모든 자막

      for i in range(0, len(all_caption)):
          if all_caption[i].code == 'ko':
                ko_sub = all_caption[i].generate_srt_captions()
                print(ko_sub)
          else:
                print('Korean Sub does not exist')
