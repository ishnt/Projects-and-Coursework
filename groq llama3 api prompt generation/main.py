from groq import Groq
import re
import streamlit as st
st.title("Youtube Shorts and Reel Scripter")
script_input = st.text_area("Enter your Topic here:")

temperature1 = st.sidebar.slider("Temperature", min_value=0.0, max_value=2.0, step=0.01, value=1.0)
max_tokens1 = st.sidebar.slider("Max Tokens", min_value=0, max_value=8192, step=1, value=8192)
top_p1 = st.sidebar.slider("Top P", min_value=0.0, max_value=1.0, step=0.01, value=1.0)
seed1 = st.sidebar.number_input("Seed", value=909016, step=1)

def generate_prompt(topic):
    prompt="""Generate one amazing attention catching , brain shocking long-form with paragraph around script for" viral reels or shorts on the topic-\""""+topic+"""""}\"  \nfinetune ur answer with these few-shot-prompts \n[\n    {\n         \"Hook\": \":Multiple big creators stole my content and got millions of views, more views than even me, the original creator.\",\n        \"Build Up\": \"Multiple big creators stole my content and got millions of views, more views than even me, who is the original. Now, I could be mad at them, but I'm a giver and I will give you two of the best ways to find wild content they shouldn't steal, but use as inspiration.\",\n        \"Body \": \"Multiple big creators stole my content and got millions of views, more views than even me, who is the original. Now, I could be mad at them, but I'm a giver and I will give you two of the best ways to find wild content they shouldn't steal, but use as inspiration. First is Tweet Hunter. Find a creator on Twitter in your space and go to their profile. Tweet Hunter will organize all the tweets by the most likes on the sidebar on the right. Scroll through and specifically look for Twitter threads. These are gold mines for video ideas. The second method is source TikTok. Find a creator on TikTok and use a Chrome extension to sort all their videos by the most views. Comment PB below if you want me to send you a link to these tools, plus a 22-page doc on how to grow your personal brand from scratch.\",\n        \"CTA\": \"Comment PB below if you want me to send you a link to these tools, plus a 22 page doc on how to grow your personal brand from scratch.\"\n    },\n    {\n        \"Hook\": \"Can you follow MrBeast on TikTok? Comment the word mud. Just comment the word wallet. Comment the word YT and... You might have noticed something there. This is the secret to how the biggest creators grow millions of followers each week.\",\n        \"Build Up\": \"This is the secret to how the biggest creators grow millions of followers each week. I personally gained 300,000 followers off one video from this method. And it's not because of their content, anyone can do this. It's because of one simple tactic you're missing out on. And that's a CTA. You see, the problem today is that people are mindlessly scrolling through social media.\",\n        \"Body \": \"Can you follow MrBeast on TikTok? Comment the word mud. Just comment the word wallet. Comment the word YT and... You might have noticed something there. This is the secret to how the biggest creators grow millions of followers each week. I personally gained 300,000 followers off one video from this method. And it's not because of their content, anyone can do this. It's because of one simple tactic you're missing out on. And that's a CTA. You see, the problem today is that people are mindlessly scrolling through social media. And if your content is getting millions of views, it's important to remind these people to take action after the video. Whether that's giving value, selling a course, doing whatever. Tell them to like, comment, share, save, everything, after the video is over. Because this simple strategy is getting people millions of followers, millions of leads, millions of dollars from their bank account. And there's endless amounts of ways to incorporate CTAs throughout your videos. I put together a vlog explaining how I grew to almost 1,000,000 followers in 2 months, So comment down below CTA if you want it.\",\n        \"CTA\": \"So comment down below CTA if you want it.\"\n    },\n    {\n        \"Hook\": \"\\\"My name is Devin Jatto and as a social media manager I charge my clients from anywhere from 53 thousand to 187 thousand dollars per year and today I'm going to share with you my favorite social media strategy so you can steal it and implement it for yourself!\\\"\",\n        \"Build Up\": \"\\\"First, you need to get clear on what you're an expert on... So for this video let's say you're a fitness coach.\\\"\",\n        \"Body \": \"\\\"Within the niche of fitness you're creating 8 different sub-topics. This is your lifetime supply of content ideas so let's start with your first sub-topic weight-loss. Head over to QUORA.com and search weight loss. Now on the left filter your search by questions. Now take at least 30 ideas and put them into some sort of spreadsheet. And in that spreadsheet create 3 different columns. Sub-topic, video idea, and view count. For 30 days create and post one idea every single day and then track the performance of each of the video's views.\\\"\",\n        \"CTA\": \"\\\"At the end of these 30 days sort your videos by most viewed to least viewed then double down on the sub-topics that performed the best! If you do this I promise that you'll grow your account!\\\"\"\n    },\n    {\n        \"Hook\": \"\\\"If you need content ideas for TikToks or Instagram reels, don't be an ass and ask ChadGBT.\\\"\",\n        \"Build Up\": \"\\\"Can you give me 10 content ideas? That's horrible. Let me put you on game and teach you how to use ChadGBT correctly to get viral content ideas.\\\"\",\n        \"Body \": \"\\\"Right now there are 800 million YouTube videos to steal ideas from. And that's exactly what we're going to do, shine AI. Head over to YouTube and search for a video within your industry. Once you find a YouTube video that you like, go ahead and copy that video's link and head over to youtubetranscript.com and paste in that video... [Instructions continue on how to convert a YouTube transcript into a content idea using AI].\\\"\",\n        \"CTA\": \"\\\"You can either screenshot this or just comment the word 'wallet' and I'll just send it over to you.\\\"\"\n    },\n    {\n        \"Hook\": \"\\\"This is how the algorithm works on social media.\\\"\",\n        \"Build Up\": \"\\\"Once you learn the algorithm, you know the rules of the game and then you know how to win the game.\\\"\",\n        \"Body \": \"\\\"When you first publish your content, it gets distributed to 20% of your followers and to a portion of people who are not your followers but those whose interest align with your content. Then the algorithm measures your content by 2 things: Watch time and Engagement. And the platform cares more about watch time. Because the longer someone spends on their platform, the more they get paid from ads. So if a person spends time watching your content, it gets pushed to more people with similar interests. Otherwise, if the content doesn't grab the viewers' attention, it gets no boost. Also, if a person shares, comments, likes, or saves your published content, the algorithm pushes your content to more viewers, resulting in more reach and engagement from a broader audience.\\\"\",\n        \"CTA\": \"\\\"And the biggest cheat code to win this game is to follow for more value.\\\"\"\n    },\n    {\n        \"Hook\": \"\\\"Here's how to turn 1 shitty content idea into 18 viral videos.\\\"\",\n        \"Build Up\": \"\\\"And if you're questioning my competence, I grew my Instagram from 0 to 200K followers in six months by using this strategy.\\\"\",\n        \"Body \": \"\\\"The first thing we want to do is come up with a core topic. For example, let's say our core topic is fitness. Now, we want to break our core topic into three different subtopics. So, in this case, they might be diet, weightlifting, and cardio. Now these three subtopics can be broken down into six different content categories. Number one, a quick tip. Number two, industry myths. Number three, common mistakes. Number four, personal stories. Number five, common questions. And lastly, my personal favorite, number six, actionable step-by-step systems. And now we have infinite content ideas.\\\"\",\n        \"CTA\": \"As always, follow for more value.\"\n    },\n    {\n        \"Hook\": \"\\\"Here's how to transform one shitty idea into seven viral hooks for your next video.\\\"\",\n        \"Build Up\": \"Build Up:\\\"Let's say the concept for your video is protein powder.\\\"\",\n        \"Body \": \"\\\"You could put a negative spin. Protein powders should never taste this good, or you could put a positive spin. This protein shake actually tastes good and it's completely organic. You can ask a question. Do your protein shakes always taste like chalk? You can share an experience. I wanted to get big this summer, but getting in enough protein feels impossible. You can call the viewer out. If you struggle with gaining muscle, listen up. Tell them how? Here's how you can reach your protein goals and enjoy it. Or you could give social proof. Here's why Ronnie Coleman can't shut up about his protein powder.\\\"\",\n        \"CTA\": \"Save this post and follow me for more value.\"\n    },\n    {\n        \"Hook\": \"\\\"You need to be using this free software for all of your Instagram videos.\\\"\",\n        \"Build Up\": \"\\\"It's called MiniChat.\\\"\",\n        \"Body \": \"\\\"You can easily build automations that instantly respond to comments, Instagram stories, cold DMs, and so much more. I've sent 162,000 automated DMs with this software...\\\"\",\n        \"CTA\": \"Comment LEARN, and I'll send you the guide right now.\"\n    },\n    {\n        \"Hook\": \"\\\"Alex Hormozi's favorite line is 'I have nothing to sell you.' But this is such a lie.\\\"\",\n        \"Build Up\": \"\\\"He does have something to sell you, it's just not what you think. The past couple of years, Alex has been building and leveraging his personal brand, positioning himself to sell to certain people, just probably not you.\\\"\",\n        \"Body \": \"\\\"In fact, when most gurus are selling for thousands of dollars, Alex Hormozi is giving it away for free. Why? Because he wants to focus all of his time on businesses making over $3 million per year. And this is where he sells. Once you're established, he sells you on taking equity in your company and continuing to mentor you as you scale. And leveraging his personal brand to do this has helped him build acquisition.com to $150 million. But none of this would be possible without his personal brand, which is exactly why you're an idiot if you're not building yours.\\\"\",\n        \"CTA\": \"\\\"Comment yes below and I'll send you a mini course showing you exactly how to build and monetize your personal brand right now.\\\"\"\n    },\n    {\n        \"Hook\": \"\\\"You need to use this copy paste method to go viral on Instagram.\\\"\",\n        \"Build Up\": \"\\\"This is the exact strategy that I used to grow 100,000 followers in 62 days, land six videos with over one million views, all without spending a dime.\\\"\",\n        \"Body \": \"First, identify a niche that you wanna grow in and find a viral video that has five times more views than the profile has followers. This is how you know the video actually went viral. Second, take the script from the video and restructure it so that it fits your personal brand image. Now you can record yourself speaking on the script just like this, edit it together, and once you master pacing and tonality, voila, now you have yourself a viral video.\",\n        \"CTA\": \"\\\"If you wanna learn pacing and tone, comment viral below, and I'll send you lesson right now.\\\"\"\n    },\n    {\n        \"Hook\": \"\\\"If you wanna start a business online but you have no money to invest, this video is for you.\\\"\",\n        \"Build Up\": \"Build Up: \\\"The creator economy is expected to double by 2026. So you still have time.\\\"\",\n        \"Body \": \"\\\"Step one, learn to create content. Comments start and I'll send you a free course on how to do this.Step two, use card for free to create a website.Step three, use Stripe, PayPal or Gumroad to collect payments.Step four, you can organize all of your work in notion for free.Step five, after you take my free course, you can use CapCut to start making videos.\\\"\",\n        \"CTA\": \"Make sure to save this video and read the caption.\"\n    },\n    {\n        \"Hook\": \"\\\"You need to be using this free editing pack for all your videos.\\\"\",\n        \"Build Up\": \"\\\"Motion backgrounds, sound effects, transitions, luts, font, Instagram border,\\\"\",\n        \"Body \": \"export settings comment free and I'll send you the pack right now.\",\n        \"CTA\": \"Drop a 'free pack' in the comments to get your editing pack instantly!\"\n    },\n    {\n        \"Hook\": \"\\\"This guy makes over a hundred thousand dollars per month profit at 20 years old running the laziest business you can imagine.\\\"\",\n        \"Build Up\": \"\\\"This is Brady, my business partner, and here's exactly how you can replicate his success.\\\"\",\n        \"Body \": \"\\\"What he does is called growth operating which means he helps me monetize my audience. I used to suffer from a disease called broke influencer syndrome where I had a massive audience but wasn't fully monetizing it to my best ability. Brady helped me build a paid community to monetize my audience and we split the profits. - Step one, find a creator similar to me with a big audience that's not selling any digital products yet. Search the how-to hashtag on TikTok and search for creators making educational videos that are only selling physical products or nothing at all and reach out to them using the scripts and get a 50, 50 partnership. - Step two, then head over to school with a K and build a pay community for their audience. This is one of the easiest parts of the process and only will take a few hours. Post live group calls with the creator and their audience, host a course and host a community for support. - Step three, charge $100 per month for access and split the profits with the creator. Me and Brady do this to monetize my audience and really only work about two hours per day and make over 100K per month profit.\\\"\",\n        \"CTA\": \"\\\"And I made an 81 page doc explaining all of our systems and strategies in-depth and I'll send it free, just comment doc.\\\"\"\n    },\n    {\n        \"Hook\": \"\\\"Here's how you make millions by becoming a Wi-Fi money pimp.\\\"\",\n        \"Build Up\": \"\\\"This is the male's version of becoming an OF girl. Except, this is actually ethical. Instead of selling feet pics, we're going to be selling info.\\\"\",\n        \"Body \": \"\\\"I've come across a few young internet millionaires who do this. This is a proven model that has stolen from a trillion dollar industry. Step one, go to findcreators.io and find a creator with at least 10,000 followers in the educational niche. Step two, reach out to the creators and use the script and the link in my bio to get them to partner with you and pimp them out for their audience. Step three, use chat-GPT and tell it to write an outline for a course educating the creators' audience about whatever niche they're in. Step four, go to Skool.com and build an info product community and sell access to it to their audience for $100 to $2,000.\\\"\",\n        \"CTA\": \"DM me 'Doc' and I'll send it to you for free.\"\n    },\n    {\n        \"Hook\": \"\\\"Have you ever wondered how much your favorite influencers make?\\\"\",\n        \"Build Up\": \"\\\"Well, I'm a Pocket Watcher and today we're gonna be pocket watching Hamza.\\\"\",\n        \"Body \": \"\\\"He is over 2.29 million subs on YouTube and runs a paid community to monetize his audience. It's called Adoma School and he charges $129 per month for access and it looks like he has 1200 people paying for access making him over $150,000 every single month. A paid community is the best business model anyone can run to monetize an influencer's audience and there is a massive opportunity for anyone to tap into this industry even if they aren't an influencer. There's millions of influencers out there with massive audiences that aren't currently monetizing their audience and anyone can partner with an influencer and help them build a paid community to monetize their audiences and split the profits with the influencer. Even if you only took 10% from helping Hamza monetize his audience that would be 15K a month and I made a free guide explaining exactly how I did this and made over $100,000 profit last month and showing you exactly how you can do the same.\\\"\",\n        \"CTA\": \"\\\"Comment Hamza and I'll send it to you for free.\\\"\"\n    },\n    {\n        \"Hook\": \"\\\"Alex Ramosi's new challenge is the simplest path to $10,000 a month.\\\"\",\n        \"Build Up\": \"\\\"Alex Ramosi recently made his biggest investment yet into School.com. He's now a co-owner of School and hosting a challenge that will give you an opportunity to meet him in person while also allowing you to make a fat stack.\\\"\",\n        \"Body \": \"\\\"Ramosi himself said that running a paid community is the simplest business model that you can run in 2024. And I couldn't agree more. You don't need any startup cash, any business experience, and you don't need an audience or need to make content. This is the same business model that I used to make 263K as a senior in high school, and over $250,000 in revenue just last month at the age of 19.\\\"\",\n        \"CTA\": \"\\\"Comment Ramosi and I'll send it for free.\\\"\"\n    },\n    {\n        \"Hook\": \"\\\"Most important rule for life: Don't complain about anything...\\\"\",\n        \"Build Up\": \"\\\"...if it's within your control, go do something about it, and if it's not within your control, you're just wasting energy.\\\"\",\n        \"Body \": \"\\\"Talking about it or thinking about it, there's a Chinese proverb that says 'The man who blames others has a long way to go, the man who blames himself is halfway there, the man who blames no one has already arrived.'\\\"\",\n        \"CTA\": \"\\\"For more life rules and wisdom, follow us for daily inspiration.\\\"\"\n    },\n    {\n        \"Hook\": \"\\\"Three tiny habits that dramatically upgraded my life.\\\"\",\n        \"Build Up\": \"\\\"Number one, no phone within 30 minutes of waking up in the morning.\\\"\",\n        \"Body \": \"The main subject of the video focuses on three life-changing habits:1. Avoiding phone use for the first 30 minutes of the day to prevent mental and physical health issues caused by an immediate surge in cortisol from stress.2. Using grayscale mode on the phone for 90% of the day to reduce the addictive nature of the colorful screen and minimize distractions.3. Implementing the \\\"one-one-one\\\" journaling method each day by noting one win, one point of gratitude, and one point of stress or anxiety, which helps to focus on the positives and maintain mental balance.\",\n        \"CTA\": \"\\\"Try these habits for a week and comment your progress!” or “Follow for more life-improving tips.”\"\n    },\n    {\n        \"Hook\": \"\\\"This Stanford Business School experiment blew my mind.\\\"\",\n        \"Build Up\": \"\\\"There was a Stanford Business School professor who gave three groups of students $5 and two hours to make the highest ROI possible on the money.\\\"\",\n        \"Body \": \"\\\"The first group went out and basically bartered with the money and they made a decent return on their money. The second group went out and realized that the $5 was actually a distraction and that what they really had was two hours to make as much money as possible. The third group was the smartest group though. They realized the presentation that would be done in front of an entire group of Stanford Business School students was the most valuable asset in the entire experiment. So, they called a bunch of local companies and sold the 30-minute presentation as advertising space and made an astronomical return.\\\"\",\n        \"CTA\": \"\\\"Now, the whole moral of this story is that you need to think differently about the problems that you're faced with. That way of thinking differently allowed them to achieve the asymmetric outcomes that we're all looking for in life.\\\"\"\n    },\n    {\n        \"Hook\": \"Teenagers are spending 70% less time with their friends in person than they were two decades ago.\",\n        \"Build Up\": \"How can you possibly build a happy, healthy, fulfilling life if your entire life is by yourself with your phone?\",\n        \"Body \": \"Scrolling on Tik Tok, scrolling on Instagram, seeing lives that aren't real out there and comparing yourself to that the entire time. Social media is a drug that is specifically designed to make you feel less about yourself. It's designed to make you wish you were somewhere else, someone else with someone else, doing something else.\",\n        \"CTA\": \"So, it’s time to put down the phone and start living in the real world - connect with your friends, engage in physical activities, and build real-life memories. Share this with someone who needs to hear it! #RealConnections\"\n    },\n    {\n        \"Hook\": \"\\\"But the beautiful thing about life is that you get to choose your hard.\\\"\",\n        \"Build Up\": \"\\\"Everything in life is hard but you get to choose what your hard is.\\\"\",\n        \"Body \": \"\\\"It's really hard to build an incredible body and physique. It's also really hard to see your body completely fail you. It's really hard to build meaningful relationships. It's also really hard to live on the surface with a bunch of people. Again, you get to choose your hard. It's really hard to live a life of purpose working on something you care about. It's also really hard to live without purpose. You get to choose the thorns that you're gonna have on the path of your journey.\\\"\",\n        \"CTA\": \"\\\"How can I just endure this a little bit longer? How can I just embrace this hard of whatever it is that I'm going through?\\\"\"\n    },\n    {\n        \"Hook\": \"\\\"Call it the one-one-one method,\\\"\",\n        \"Build Up\": \"\\\"which is every single night before you go to bed,\\\"\",\n        \"Body \": \"sit down with a piece of paper and write down one win from the day, one point of tension or anxiety or stress, and then one point of gratitude. It takes two minutes. And you immediately feel good about the win and you register some wind that you had during the day. You get off your mind the crappy thing that's been bugging you that's gonna bug you. For me, like I won't be able to sleep, I'll be thinking about it. Just throw it down on paper; it's gone, it's out of your mind. Then you feel grateful for some small thing that you otherwise would have just let blow by that you never would have thought about. It creates a journaling habit that actually kind of moves you forward without taking a bunch of time.\",\n        \"CTA\": \"The original script does not include a clear Call to Action (CTA).\",\n\"Hook\": \"\\\"If you're an entrepreneur, you chose this path because you want to produce amazing results in living an amazing life.\\\"\",\n        \"Build Up\": \"\\\"That requires patience and grit. Great things don't happen overnight.\\\"\",\n        \"Body \": \"\\\"Time is not your most important asset. Energy is. Because even if you have hundreds of free hours, you won't use that time well if you don't have energy and motivation. Here are three simple ways that I optimize my energy so that I can use my time in meaningful ways.\\\"1. \\\"Take a break and lift weights. I lift weights five days a week...\\\"2. \\\"No meetings until 2 PM. So many people want our attention and the ability to focus on ourselves is the number one key to success...\\\"3. \\\"Iced Americano. My morning cup of coffee is my daily highlight...\\\"\",\n        \"CTA\": \"\\\"I wait around 90 minutes after waking up to drink caffeine to prevent an afternoon crash.\\\"\"\n    },\n    {\n        \"Hook\": \"\\\"Did you know that up until May 6, 1954, it was universally accepted that the human body simply could not run a mile in less than 4 minutes?\\\"\",\n        \"Build Up\": \"But then Roger Bannister, a 25 year old medical student, made history.\",\n        \"Body \": \"By running a mile in 3 minutes and 59 seconds, Bannister not only shattered a physical record, he broke a psychological barrier, changing the belief system of athletes worldwide. After his sprint, numerous other athletes broke the 4-minute barrier as well, proving that the once 'impossible' was indeed possible.\",\n        \"CTA\": \"\\\"We all have our own 4-minute mile. Find and befriend those who have achieved your 'impossible'. Let their success inspire you to break your own barriers. Remember, what feels unattainable can often be overcome with a mindset shift and the right company. Who will you surround yourself with?\\\"\"\n    },\n    {\n        \"Hook\": \"\\\"Are you grateful to be alive? You should be.\\\"\",\n        \"Build Up\": \"\\\"Your chances of being born require 2 parents, 4 grandparents, 8 great-grandparents,\\\" leading up to \\\"2,048 9th-great grandparents.\\\"\",\n        \"Body \": \"\\\"And that only takes us back to about the 17th century. Imagine the amount of challenges, struggles, and battles your thousands of ancestors faced and conquered so that you could be alive today.\\\"\",\n        \"CTA\": \"Be grateful and honour your ancestors by doing something awesome in your life.\"\n    },\n    {\n        \"Hook\": \"\\\"So, the real second sauce is Audible, one of the largest companies in the world for subscription service, selling what is arguably information, right?\\\"\",\n        \"Build Up\": \"\\\"Do you know how their system works? How people read books on Audible? Have you ever used it before?\\\"\",\n        \"Body \": \"\\\"Oh, they have credits. They have credits. Yeah. Why do they have credits? To get recurring revenue. Because if somebody came in and they could get 500 books the first day, either they'd get 500 books the first day and then they'd cancel the membership the next month. Right, right, right. Or they'd be so overwhelmed, they wouldn't know what to do that they would literally just cancel the subscription. There's no way I'm getting my value out of this. So give them a credit each month. I give them a credit every month. And so we built in a full custom code system that gives people credits every month.\\\"\",\n        \"CTA\": \"\\\"And then I have a video called The Theory of Constraints Video. I'm just giving it away all on this. And it literally says, okay, from if you're a beginner and you have zero money and no offer, all the way to you're doing $1 million dollars a month, these are the different problems you're gonna have and these are the different classes that solve these problems.\\\"\"\n    },\n    {\n        \"Hook\": \"\\\"Most people don't have businesses. They have promotions.\\\"\",\n        \"Build Up\": \"\\\"They live on a revenue roller coaster where one month is high and the other month is a complete low. And the reason they have this is because they're solely focused on marketing and getting upfront cash as quickly as possible.\\\"\",\n        \"Body \": \"\\\"What I've learned after generating tens of millions of dollars online is that, in order to shift from that promotional rollercoaster that most people find themselves on into a real business with enterprise value, you need two main things. The first is product led growth, and that's when your products sell themselves and ascend people into traditional products or services without you having to do any work. [...] And the second part of it is that you want to have recurring revenue. [...] So we launched a membership site. About 90 days ago at this point. And we're generating tens of thousands of dollars a month.\\\"\",\n        \"CTA\": \"(Implicit) By sharing the speaker's personal success with the approach, the call-to-action is implied rather than directly stated. The viewer is led to consider implementing the same strategies of product led growth and recurring revenue models for their own business, but there is no direct action like \\\"click here\\\" or \\\"sign up now\\\". It may prompt viewers to look into the speaker's methods or contact them for further information.\"\n    },\n    {\n        \"Hook\": \"\\\"I treat my relationship with my girlfriend like a business and it's made my life 100 times better\\\"\",\n        \"Build Up\": \"\\\"Here are a few things that we do\\\"\",\n        \"Body \": \"\\\"The first is that we have a bi-weekly meeting with an agenda on this agenda We're covering things like sharing the wins from the past two weeks, both personal and professional We go through each other's life visions or life manifestos. So we make sure those things are aligned We review our quarterly goals and rocks, which I'll talk about in a second here. And then we discuss any issues that we're going through we feel like the other person isn't noticing Or that we want to solve and we solve them once and for all on that call Creating a safe environment for us to kind of knock forward in our relationship. The second system we set up is a quarterly goal setting system myself and my partner We both want to be people that are always progressing forward And so every single quarter we set a goal and we put it inside of Asana and we track it on those bi-weekly meetings. So, for example, my goal last quarter was to create an elevated wardrobe that has an elevated style That gets me compliments everywhere I go and I was able to do that and then my girlfriend's hers was that she wanted to create a money-making Opportunity that she felt fulfilled Doing and that she was generating money from by the end of the quarter and she did that when she launched a membership site. So we both were able to add and help each other along the goals setting process And we were holding each other accountable. The third way I treat my relationship Like a business is making sure we have crystal clear communication So what I've learned managing dozens of employees is even just one or two words wrong Message in email a text message or on a call could have disastrous implications.\\\"\",\n        \"CTA\": \"The script provided does not contain a clear CTA (call to action).\"\n    },\n    {\n        \"Hook\": \"\\\"Here are the three employees you need to scale from six figures to seven figures.\\\"\",\n        \"Build Up\": \"\\\"The first is gonna be a virtual assistant. And actually a few years ago, I placed over 2,000 virtual assistants for businesses online.\\\"\",\n        \"Body \": \"\\\"And that was because virtual assistants were a really easy way to take whatever the business owner was already doing and just do more of it and remove the business owner from it. So what are the you're doing cold email every day, you're doing cold calls every day, you're setting up ad accounts for your clients every single day, whatever the thing that you're doing every single day, that is just kind of busy or administrative work. And that's just repetitive. If you can't automate it, you should hire a virtual assistant for three to $5 an hour and have them do that task for you, getting back your time.The second person is gonna be a salesperson. Now, a lot of people freak out about hiring a salesperson, but it's really easy to do once you have an optimal selling system. So once you already are getting a certain amount of people from a certain kind of structure, whether it's a video call Funnel, a cold call, an email, you have a little bit of a system behind it. You wanna hire a sales person because although you're gonna have to pay them 10% of your sales, it's gonna get you back six to eight hours a day to get more appointments on your calendar to then hire more sales people to be able to scale.And the third person should be a video editor. Now, if you're not creating videos, you definitely need to in today's day and age. It's how you can build trust with your prospects before they even get on a call with you to begin with. And so, editing videos is a pretty difficult thing to do. It's funny to me when I work with some of my clients that have millions of subscribers on YouTube, they're still editing their own videos. And some of them say they like doing it, which is fine.\\\"\",\n        \"CTA\": \"The script provided does not include a clear Call-To-Action.\"\n    },\n    {\n        \"Hook\": \"\\\"So how do you know when it's time to scale up ads versus scaling them down?\\\"\",\n        \"Build Up\": \"The build-up reinforces the hook's question by addressing a common misconception and leading the viewers to a sense of anticipation for the explanation: \\\"And why would you even want to scale down ads in the first place, right?\\\"\",\n        \"Body \": \"\\\"So you scale up ads when you have the first signs of a positive indication... As soon as I started seeing quality sales calls being booked on the calendar...quality people are being booked on the counter from the ads... And now when do you want to scale back ads? I just had a call with a client yesterday who actually cut their ad spend considerably by almost 80%...they weren't able to keep up with client success.\\\"\",\n        \"CTA\": \"\\\"But once you do have a problem with client success, you need to address it immediately because the worst thing that can happen is you keep on scaling up your ads. You're not able to deliver on the client success and then you start getting a bad word of mouth.\\\"\"\n    },\n    {\n        \"Hook\": \"\\\"So, how do you separate yourself from your competition? Especially if you guys are offering essentially the exact same thing.\\\"\",\n        \"Build Up\": \"\\\"Well in truth, what you need to create is something called a unique mechanism.\\\"\",\n        \"Body \": \"\\\"And a unique mechanism is exactly that—it is a unique way that you are going to deliver results for your clients that's different than how your competitors do it. We just don't extract it and market it in our top of funnel marketing. If you're able to create a word or phrase that describes your process, then in doing so, you will separate yourself from other people who haven't created that word or phrase. For example, in my industry, there are a lot of people that help other people scale their businesses. But in our business, we have a few unique mechanisms such as the self-sustaining funnel, which is a concept or idea I've created on how to build an entire marketing system that feeds itself. Another example of a unique mechanism for our company is the member method, which is how we use subscription membership services to fuel our high-ticket businesses.\\\"\",\n        \"CTA\": \"\\\"So you could say that some of these things aren't radical or totally different, but it's because I have extracted them from our processes and put a name around them, that it separates us from our competition.\\\"\"\n    },\n    {\n        \"Hook\": \"\\\"If you're trying to get to $100,000 a month...\\\"\",\n        \"Build Up\": \"\\\"...the fastest path to do that is to simply learn the solutions to the problems, create systems around them...\\\"\",\n        \"Body \": \"\\\"...and sell it to a business owner in a consulting slash value-creator model. What you're gonna do is you're gonna figure out what is everything necessary to take a client from point A to point B. Point A maybe is $1000 a month and you want to take your client to $10,000 a month or maybe they're a hundred leads a month and you want to get them to 500 leads a month.\\\"\",\n        \n    \n   \n    \n    }\n]"""

    return prompt
if st.button("SCRIPT"):
    a=generate_prompt(script_input)
    print(a)
    client = Groq()
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": a
            },
            {
                "role": "user",
                "content": "write"
            }
        ],
        temperature=temperature1,
        max_tokens=max_tokens1,
        top_p=top_p1,
        stream=False,
        stop=None,
        seed=seed1
    )
    
    answer=completion.choices[0].message.content
    st.write(answer)


