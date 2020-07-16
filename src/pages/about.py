"""Home page shown when the user enters the application"""
import streamlit as st

import awesome_streamlit as ast


# pylint: disable=line-too-long
def write():
    """Used to write the page in the app.py file"""
    with st.spinner("Loading About ..."):
        ast.shared.components.title_awesome("")

    st.subheader("About Us")
    st.write(
      """
      We are a group of individuals who found each other on the way to a Hackathon, where we
discovered our common interests in solving the real world problems. The group that got formed
in the year 2019, sought to take up the IBM HackChallenge 2020.

The prime motive of the problem statement was to manage the warehouse for perishable goods.
Perishable food becomes an important factor that costumer may consider while choosing
one retail store among others. The increasing demand for perishable food leads to a higher
profit, meanwhile, larger companies and a variety of food items impose further challenges.
The mass spoilage and difficulty in management impel retailers to set a higher retail price.
The deterioration because of demand uncertainty of perishable items result in a large portion
of the items being unsalable. So this site can manage this problem under your fingertips.
Management bridges the gap between demand and supply. We have understood this. The site
follows a gradient boosting technique to provide proper visualization to understand the changing trends
in demand and predicting them. This can be a way out of the problem because knowing the demand
can only help in knowing the supply and hence balance the management for optimization of
perishable foods.

      """
    )

        

       
    st.subheader("Our Team")
    st.write(
    f'<html lang="en" >'
    '<head>'
    '<meta charset="UTF-8">'
    '<title>CodePen - Profile Card UI Design Cool Hover Effect</title>'
    "<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.2/css/bootstrap.min.css'>"
    "<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'>"
    '<style>'

    'body {'
    'font-family: tahoma;'
    'url(https://picsum.photos/g/3000/2000);'
    'height: 50vh;'
    'background-size: cover;'
    'background-position: center;'
    'display: flex;'
    'align-items: center;'
  '}'

  '.our-team {'
  '  padding: 30px 0 40px;'
  '  margin-bottom: 30px;'
  '  background-color: #f7f5ec;'
  '  text-align: center;'
  '  overflow: hidden;'
  '  position: relative;'
  '}'

  '.our-team .picture {'
  '  display: inline-block;'
  '  height: 130px;'
  '  width: 130px;'
  '  margin-bottom: 50px;'
  '  z-index: 1;'
  '  position: relative;'
  '}'

  '.our-team .picture::before {'
  '  content: "";'
  '  width: 100%;'
  '  height: 0;'
  '  border-radius: 50%;'
  '  background-color: #1369ce;'
  '  position: absolute;'
  '  bottom: 135%;'
  '  right: 0;'
  '  left: 0;'
  '  opacity: 0.9;'
  '  transform: scale(3);'
  '  transition: all 0.3s linear 0s;'
  '}'

  '.our-team:hover .picture::before {'
  '  height: 100%;'
  '}'

  '.our-team .picture::after {'
  '  content: "";'
  ' width: 100%;'
  '  height: 100%;'
  '  border-radius: 50%;'
  '  background-color: #1369ce;'
  '  position: absolute;'
  '  top: 0;'
  '  left: 0;'
  '  z-index: -1;'
  '}'

  '.our-team .picture img {'
  '  width: 100%;'
  '  height: auto;'
  '  border-radius: 50%;'
  '  transform: scale(1);'
  '  transition: all 0.9s ease 0s;'
  '}'

  '.our-team:hover .picture img {'
  '  box-shadow: 0 0 0 14px #f7f5ec;'
  '  transform: scale(0.7);'
  '}'

  '.our-team .title {'
  '  display: block;'
  '  font-size: 15px;'
  '  color: #4e5052;'
  '  text-transform: capitalize;'
  '}'

  '.our-team .social {'
  '  width: 100%;'
  '  padding: 0;'
  '  margin: 0;'
  '  background-color: #1369ce;'
  '  position: absolute;'
  '  bottom: -100px;'
  '  left: 0;'
  '  transition: all 0.5s ease 0s;'
  '}'

  '.our-team:hover .social {'
  '  bottom: 0;'
  '}'

  '.our-team .social li {'
  ' display: inline-block;'
  '}'

  '.our-team .social li a {'
  ' display: block;'
    'padding: 10px;'
    'font-size: 17px;'
    'color: white;'
    'transition: all 0.3s ease 0s;'
    'text-decoration: none;'
  '}'

  '.our-team .social li a:hover {'
  ' color: #1369ce;'
    'background-color: #f7f5ec;'
  '}'
  '</style>'
  '</head>'
  '<body>'
  '<!-- partial:index.partial.html -->'
  '<div class="container">'
    '<div class="row">'
      '<div class="col-12 col-sm-6 col-md-4 col-lg-3">'
      '  <div class="our-team">'
      '    <div class="picture">'
      '      <img class="img-fluid" src="https://media-exp1.licdn.com/dms/image/C4D03AQHJNWR7TSqwLQ/profile-displayphoto-shrink_400_400/0?e=1599696000&v=beta&t=S29M6i9-J4O7uwwxYbvD1KacBf522o8gGME2RBnQU3c">'
      '    </div>'
      '    <div class="team-content">'
      '      <h3 class="name">Ashish Sureka</h3>'
      '      <h4 class="title">&emsp;&emsp;Tech-&emsp;&emsp;Enthusiast</h4>'
      '    </div>'
      '    <ul class="social">'
      '      <li><a href="https://twitter.com/Ashish_Sureka_" target="_blank" class="fa fa-twitter" aria-hidden="true"></a></li>'
      '      <li><a href="https://www.linkedin.com/in/ashish-sureka/" target="_blank" class="fa fa-linkedin" aria-hidden="true"></a></li>'
      '    </ul>'
      '  </div>'
      '</div>'
      '    <div class="col-12 col-sm-6 col-md-4 col-lg-3">'
      '  <div class="our-team">'
      '    <div class="picture">'
      '      <img class="img-fluid" src="https://media-exp1.licdn.com/dms/image/C5103AQE-c19itCKVsw/profile-displayphoto-shrink_400_400/0?e=1599696000&v=beta&t=OIeSYnWq7TH3ba1R-q746MoEoYfjCJq32eVtMlIIvrI">'
      '    </div>'
      '    <div class="team-content">'
      '      <h3 class="name">Debidutta Dash</h3>'
      '      <h4 class="title"> &emsp;&emsp;Tech-&emsp;&emsp;Enthusiast</h4>'
      '    </div>'
      '    <ul class="social">'
      '      <li><a href="https://twitter.com/Dddash11Dev" target="_blank" class="fa fa-twitter" aria-hidden="true"></a></li>'
      '      <li><a href="https://www.linkedin.com/in/debidutta-dash/" target="_blank" class="fa fa-linkedin" aria-hidden="true"></a></li>'
      '    </ul>'
      '  </div>'
      '</div>'
      '    <div class="col-12 col-sm-6 col-md-4 col-lg-3">'
      '  <div class="our-team">'
      '    <div class="picture">'
      '      <img class="img-fluid" src="https://media-exp1.licdn.com/dms/image/C5103AQFUTppzklX5Hw/profile-displayphoto-shrink_400_400/0?e=1599696000&v=beta&t=2Xc9iK3QBegIDnFw8wzOQQGtd5yxpu4ygxV1tFrDRHo">'
      '    </div>'
      '    <div class="team-content">'
      '      <h3 class="name">Deekshya Dash</h3>'
      '      <h4 class="title"> &emsp;&emsp;Tech-&emsp;&emsp;Enthusiast</h4>'
      '    </div>'
      '    <ul class="social">'
      '      <li><a href="https://twitter.com/Deekshya_dash" target="_blank" class="fa fa-twitter" aria-hidden="true"></a></li>'
      '      <li><a href="https://www.linkedin.com/in/deekshya-dash-84570a17a/" target="_blank" class="fa fa-linkedin" aria-hidden="true"></a></li>'
      '    </ul>'
      '  </div>'
      '</div>'
      '    <div class="col-12 col-sm-6 col-md-4 col-lg-3">'
      '  <div class="our-team">'
      '    <div class="picture">'
      '      <img class="img-fluid" src="https://media-exp1.licdn.com/dms/image/C4D03AQHU-1iZHkn8bg/profile-displayphoto-shrink_400_400/0?e=1599696000&v=beta&t=A_qry-lFpHHpO7gW2rnzeEfArEFNN6WVE3zp0BrDzcQ">'
      '    </div>'
      '    <div class="team-content">'
      '      <h3 class="name">Sanjam Panda</h3>'
      '      <h4 class="title">&emsp;&emsp;Tech-&emsp;&emsp;Enthusiast</h4>'
      '    </div>'
      '    <ul class="social">'        
      '      <li><a href="https://twitter.com/sanjam_008" class="fa fa-twitter" target="_blank" aria-hidden="true"></a></li>'        
      '      <li><a href="https://www.linkedin.com/in/sanjam-kumar-panda-543141168/" target="_blank" class="fa fa-linkedin" aria-hidden="true"></a></li>'
      '    </ul>'
      '  </div>'
      '</div>'
    '</div>'
  '</div>'
  '<!-- partial -->'
    
  '</body>'
  '</html>',
  unsafe_allow_html=True)

    
    st.header("&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Credits ")

    st.write(
      """
      - [Image](https://onefamily.ie/wp-content/uploads/2019/12/img_ed7460393073e6b0abab4a69b572f0bc_1512388377925_processed_original.jpg) used in Home Page

      - This UI is inspired from [Awesome Streamlit](https://awesome-streamlit.org/)

      

      """
    )
    st.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    st.write("Github Repository link for this project. Click [here](https://github.com/SmartPracticeschool/SBSPS-Challenge-2674-Optimized-Warehouse-Management-of-Perishable-Goods-for-a-Food-Delivery-Company.git)")
    
    
    
    
    st.subheader("&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;Made with 🖤 by CodeKids  ")
