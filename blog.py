import streamlit as st

# Streamlit page setup
st.set_page_config(page_title="Negative Effect of Social Media", layout="centered")
st.title("Negative Effect of the Social Media")

# Display the picture using Streamlit
st.image("pic1.png", width=250, caption="Picture of the writer")  # Make sure pic1.png is in the same folder as app.py

# HTML content WITHOUT the <img src="pic1.png"> tag
html_content = """
<!DOCTYPE html>
<html>
<head>
  <title>NEGATIVE EFFECT OF THE SOCIAL MEDIA</title>
</head>
<body bgcolor="#FFFFFF">

<h3><i><u>AN ARTICLE PUBLISHED BY A GHANAIAN STUDENT.</u></i></h3>

<p>
  Owusu Prince Boateng is my name from Dasein, Pokuasae Branch. You and I, we've heard of 
  <mark style="background-color:#00FF00"><b><i><u>social media</u></i></b></mark>
  and we are available on those medias, popular ones are.
  Due to my limited time, let me dive you into the negative aspect since we don't give much attention to 
  but affects us in a way we don't see it. You can share your thought with me on <a href="#">poboat25@gmail.com</a>.
  <i><b>Now let's zero in on the effects!!</b></i>
</p>

<br>
<b><u>The Double-Edge Sword of Social Media</u></b><br>
<p>
Social media has woven itself into the fabric of modern life, transforming how we communicate, share and perceive the world. Platforms like
<a href="#">Facebook</a>,
<a href="#">Instagram</a>,
<a href="#">Twitter(X)</a> and
<a href="#">Tiktok</a>
have become essential tools for staying connected, building communities and consuming content. However, beneath their seemingly harmless interface lies a complex web of effects — both positive and negative — that shape our mental health, relationships and society at large.
</p>

<p>
<b>THE DARK SIDE: Mental and Emotional Impacts</b><br>
<ul>
  <li><b>Mental Health Concern:</b></li>
</ul>
Studies link excessive social media use to anxiety, depression, and loneliness. Constant comparison to curated content can erode self-esteem and breed insecurity.<br>
We all have borne witness to such effects. Some content can have a mental impact on the viewer. A content creator may expose various parts of her body, and a viewer might think,
<i>"Oh this is nothing, it's even better."</i> The next time, she might copy that creator due to the likes and comments received.
</p>

<p>
Not going to talk much on this point since most of us are included — "HAHAHA".<br>
Algorithms on social media are designed to keep users engaged, often leading to compulsive scrolling and reduced productivity. Once you're online, it's hard to log out unless you're out of data.
Those who are victims know what I'm saying — "gotcha! you're smiling".
</p>

<p>
<ul>
  <li><b>Cyberbullying:</b></li>
</ul>
The anonymity of the internet can embolden harmful behaviours, leaving victims emotionally and psychologically scarred.<br>
This reminds me of a video I saw online. Two girls insulted a woman publicly. Apparently, the woman had a beef with their friend. The woman threatened to curse them — and she did. Later, one of the girls died mysteriously. The other, scared, came online crying and seeking forgiveness — but the woman refused.
</p>

<p>This is a clear example of emotional and psychological trauma.</p>

<p>
<ul>
  <li><b>Misinformation:</b></li>
</ul>
False or misleading content spreads rapidly, influencing public opinion and even swaying elections.<br>
We know media can spread false information. Recently, I heard that the price of cement had reduced — but it turned out to be false.
<p>You’ve been in my shoes before, right?</p>
</p>

<p>
<b>THE DARK SIDE 2: Social And Cultural Ramifications</b><br>
<ul>
  <li><b>Polarization:</b></li>
</ul>
Social media algorithms often prioritize content that aligns with users' beliefs, reinforcing echo chambers and deepening divides.
</p>

<p>
<ul>
  <li><b>Privacy Concerns:</b></li>
</ul>
Platforms collect vast amounts of personal data, raising concerns over surveillance, data breaches, and consent.<br>
I recall a celebrity's private naming ceremony where guests were warned not to record. Despite that, a video surfaced. This led to a legal battle with a TV station, which was fined in court.
</p>

<p>
<ul>
  <li><b>Cultural Homogenization:</b></li>
</ul>
Certain aesthetics or trends dominate, stifling individuality and local cultures.<br>
Some trends go against traditional values, believed to have both physical and spiritual impacts.
</p>

<br><br>
<p style="color: #000000;"><b><u>THE PATH FORWARD: Balancing The Scale</u></b></p>
<p style="color: #000000;">
<b><i>Want to continue reading this article?</i></b>
</p>

<p>
<input type="radio" name="question" value="yes"> Yes<br>
<input type="radio" name="question" value="no"> No
</p>
<p>
<input type="submit" name="next_page" value="Next Page">
<input type="submit" name="previous_page" value="Previous Page">
</p>

</body>
</html>
"""

# Render the HTML content
st.markdown(html_content, unsafe_allow_html=True)
