from .models import Pitch


def get_pitches():
    pitch_list = []
    pitch_one = Pitch(title='Elevator Pitch Example for an Professional Accountant',
                      body="""
     A plumber approached me because while he’s a very good plumber he had no idea how to improve the profitability of his business.

     I set up a simple reporting system for him so his numbers are always up to date, and he can do future forecasting for his business.

     I’m happy to report that based on this information he was able to increase his profit by 17% last year.

     A great lead for me is a trade professional.
     """,
                      author='Improv Andy',
                      category='business',
                      upvotes=1,
                      downvotes=0)
    pitch_two = Pitch(title='Research Job Pitch',
                      body="""
                    Hi, my name is Samantha Atcheson, and I am a senior Environmental Sciences major. I’m looking for a
position that will allow me to use my research and analysis skills. Over the past few years, I’ve been
strengthening these skills through my work with a local watershed council on conservation strategies to
support water quality and habitats. Eventually, I’d like develop education programs on water
conservation awareness. I read that your organization is involved in water quality projects. Can you tell
me how someone with my experience may fit into your organization?
                    """,
                      author='Samantha Atcheson',
                      category='jobs',
                      upvotes=3,
                      downvotes=0)
    pitch_three = Pitch(title='Small Business', body="""
                        I'm a lawyer with the government, based out of D.C. I grew up in Ohio, though, and I'm looking to relocate closer to my roots, and join a family-friendly firm. I specialize in labor law, and worked for ABC firm before joining the government.
                        """, author='Sarah', category='Business', upvotes=0, downvotes=0)

    pitch_list.extend((pitch_one, pitch_two, pitch_three))
    return pitch_list


def get_pitch(category):
    pitches = get_pitches()
    category_list = []
    for pitch in pitches:
        if pitch.category == 'category':
            category_list.append(pitch)
    return pitch
