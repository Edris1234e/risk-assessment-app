import streamlit as st

st.title("سامانه ارزیابی ریسک")
text = st.text_area("متن ریسک را وارد کنید:")

if st.button("تحلیل ریسک"):
    # تحلیل آزمایشی ساده:
    if "مرگ" in text or "انفجار" in text:
        شدت = 5
    elif "سوختگی" in text or "شیمیایی" in text:
        شدت = 4
    else:
        شدت = 3

    احتمال = 3  # به‌صورت ثابت برای تست
    کشف = 2     # به‌صورت ثابت برای تست

    rpn = شدت * احتمال * کشف

    st.markdown(f"**شدت:** {شدت}")
    st.markdown(f"**احتمال:** {احتمال}")
    st.markdown(f"**کشف:** {کشف}")
    st.markdown(f"**عدد RPN:** {rpn}")

