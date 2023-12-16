import ContactToolHeader from './ContactToolHeader';

interface ContactToolAreaProps {
  isCheckedKakao: boolean;
  isCheckedEmail: boolean;
  toggleKakao: () => void;
  toggleEmail: () => void;
}

const ContactToolArea: React.FC<ContactToolAreaProps> = ({
  isCheckedKakao,
  isCheckedEmail,
  toggleKakao,
  toggleEmail,
}) => {
  //   const checkedRadioPath = 'assets/images/button/radio_checked.png';
  //   const uncheckedRadioPath = 'assets/images/button/radio_unchecked.png';

  return (
    <section className="self-stretch h-20 flex-col justify-start items-start gap-4 flex">
      <ContactToolHeader />

      <div className="self-stretch justify-start items-start gap-12 inline-flex">
        <div className="grow shrink basis-0 flex-col justify-center items-start gap-4 inline-flex">
          <div
            className={`justify-start items-center gap-4 inline-flex cursor-pointer ${
              isCheckedKakao ? 'text-indigo-600' : 'text-slate-300'
            }`}
            onClick={toggleKakao}
          >
            <div
              className={`w-6 h-6 rounded-sm border-2 border-slate-500 ${
                isCheckedKakao ? 'bg-indigo-600' : ''
              } ${isCheckedKakao ? 'border-none' : ''}`}
              onClick={toggleKakao}
            />
            {/* <div className="w-6 h-6 rounded-sm border-2 border-slate-500" />
            <img
              className="w-6 h-6 rounded-full "
              src={isCheckedKakao ? checkedRadioPath : uncheckedRadioPath}
              alt="Kakao"
            /> */}
            <div className="text-lg font-medium font-['SUIT'] leading-7 tracking-tight">
              문자메시지 수신
            </div>
          </div>

          {/* 핸드폰 번호 입력 필드 */}
          {/* <div
                  className={`self-stretch h-[52px] bg-slate-600 rounded-lg justify-start items-center inline-flex  ${
                    cellphoneError ? 'border border-error-primary' : ''
                  }`}
                > */}
          <div
            className={`self-stretch h-[52px] bg-slate-600 rounded-lg justify-start items-center inline-flex`}
          >
            <input
              type="text"
              placeholder="010-0000-0000"
              className={`grow self-stretch px-4 py-3 rounded-lg basis-0 text-slate-400 bg-slate-600 text-lg font-medium font-['SUIT'] leading-7 tracking-tight`}
            />
          </div>
        </div>
        <div className="grow shrink basis-0 flex-col justify-center items-start gap-4 inline-flex">
          <div
            className={`w-[167.67px] h-7 justify-start items-center gap-4 inline-flex cursor-pointer ${
              isCheckedEmail ? 'text-indigo-600' : 'text-slate-300'
            }`}
            onClick={toggleEmail}
          >
            <div className="flex items-center me-4 gap-4">
              <div
                className={`w-6 h-6 rounded-sm border-2 border-slate-500 ${
                  isCheckedEmail ? 'bg-indigo-600' : ''
                } ${isCheckedEmail ? 'border-none' : ''}`}
              />
              {/* 
              <input
                id="email-checkbox"
                type="checkbox"
                value="email"
                className={`w-6 h-6 rounded-sm border-2 border-slate-500 ${
                  isCheckedEmail ? 'bg-indigo-600' : ''
                }`}
              /> */}
              <label
                htmlFor="email-checkbox"
                className="text-lg font-medium font-['SUIT'] leading-7 tracking-tight"
              >
                E-Mail 수신
              </label>
            </div>
          </div>

          {/* 이메일 input 영역 */}
          {/* <div
                  className={`self-stretch h-[52px] bg-slate-600 rounded-lg justify-start items-center inline-flex  ${
                    emailError ? 'border border-error-primary' : ''
                  }`}
                > */}
          <div
            className={`self-stretch h-[52px] bg-slate-600 rounded-lg justify-start items-center inline-flex`}
          >
            <input
              type="email"
              placeholder="abcd@gmail.com"
              className={`grow self-stretch px-4 py-3 rounded-lg basis-0 text-slate-400 bg-slate-600 text-lg font-medium font-['SUIT'] leading-7 tracking-tight`}
            />
          </div>
        </div>
      </div>
    </section>
  );
};

export default ContactToolArea;