from moviepy.editor import VideoFileClip

video = VideoFileClip(r'C:\Users\AshutoshFulzele\Downloads\Washington DC 4K - Sunset Drive.mp4')
video = video.subclip(25)        # Starting after 25th second and cutting out last 0 seconds
video.write_videofile(r'C:\Users\AshutoshFulzele\PycharmProjects\AshProjects\Assets\Videos\CityDriving_4.mp4')

