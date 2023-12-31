interface RegisterKeywordProps {
  items: { id: number; text: string }[];
  onDeleteKeyword: (id: number) => void;
  error: boolean;
}

const RegisterKeyword: React.FC<RegisterKeywordProps> = ({
  items,
  onDeleteKeyword,
  error,
}) => {

  const handleDeleteClick = (id: number) => {
    onDeleteKeyword(id);
  };

  return (
    <div>
      <div
        className={`w-[558px] ${error ? 'mt-12' : 'mt-4'
          } mb-4 h-10 justify-start items-start gap-2 inline-flex`}
      >
        {items.map((item) => (
          <div
            key={item.id}
            className="px-4 py-1 rounded-full border border-slate-500 justify-start items-center gap-2 flex"
          >
            {/* 키워드 삭제 버튼 */}
            <div className="w-4 h-4 relative ite">
              <button
                onClick={() => handleDeleteClick(item.id)}
                className="absolute"
              >
                <img src="/assets/images/icon/x.svg" alt="Delete Keyword" />
              </button>
            </div>

            {/* 키워드명 */}
            <div className="text-white text-base font-normal font-['SUIT'] leading-7 tracking-tight">
              {item.text}
            </div>
          </div>
        ))}
      </div>

    </div>
  );
};

export default RegisterKeyword;
