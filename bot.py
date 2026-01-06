import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from openai import OpenAI

# توکن بات تلگرام (از BotFather گرفتی)
TELEGRAM_TOKEN = "8019148790:AAGyFYN_TL6oQg4zb9UbY0fZIjn4j52MDvg"

# کلید API OpenAI (از platform.openai.com گرفتی یا بعداً می‌گیری)
OPENAI_API_KEY = "AIzaSyDFAEvbSlVDZ2zsScVhtaemiWTKsCxPYxA"

client = OpenAI(api_key=OPENAI_API_KEY)
async def start(update: Update, context):
    print(f"دستور /start دریافت شد از کاربر {update.effective_user.first_name} (ID: {update.effective_user.id})")
    await update.message.reply_text(
        "سلام! 👋\n"
        "من Miss Variance هستم، منشی هوشمند کلینیک DR STATISTICS 📊\n"
        "مشکل آماری‌تون چیه؟ داده‌هاتون رو بفرستید یا سؤالتون رو بپرسید!"
    )

async def handle_message(update: Update, context):
    print(f"پیام دریافت شد: '{update.message.text}' از کاربر {update.effective_user.first_name}")
    # بقیه کد...
async def start(update: Update, context):
    await update.message.reply_text(
        "سلام! 👋\n"
        "من Miss Variance هستم، منشی هوشمند کلینیک DR STATISTICS 📊\n"
        "مشکل آماری‌تون چیه؟ داده‌هاتون رو بفرستید یا سؤالتون رو بپرسید!"
    )

async def handle_message(update: Update, context):
    user_message = update.message.text
    
    if update.message.chat.type == 'private':
        # پرامپت هوشمند برای Miss Variance
        system_prompt = (
            "تو Miss Variance هستی، منشی حرفه‌ای و صمیمی کلینیک DR STATISTICS. "
            "متخصص کمک به مشکلات آماری، تحلیل داده، تفسیر نتایج و نوبت‌دهی هستی. "
            "پاسخ‌هات رو به فارسی، واضح، مفید و با لحن گرم بده. "
            "اگر کاربر داده یا فایل فرستاد، پیشنهاد تحلیل بده. "
            "اگر نیاز به نوبت باشه، بگو چطور رزرو کنن."
        )
        
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",  # مدل ارزان و سریع
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.7
            )
            ai_reply = response.choices[0].message.content
            await update.message.reply_text(ai_reply)
        
        except Exception as e:
            await update.message.reply_text("متأسفانه مشکلی پیش اومد. دوباره امتحان کنید یا بعداً پیام بدید 🙏")

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Miss Variance در حال اجراست... 🚀")
    app.run_polling()

if __name__ == '__main__':
    main()