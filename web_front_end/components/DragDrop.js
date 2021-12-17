export default function DragDrop() {
    return (
        <div className="w-full h-[85%] flex justify-center items-center">
            <label id="file-label" for="file" className="flex opacity-1 w-[356px] h-[452px] md:w-[706px] md:h-[614px] bg-transparent border-4 border-text border-dashed rounded-xl flex-col justify-center items-center hover:cursor-pointer">
                <div className="w-64 text-text stroke-[0.5]">
                    <svg class="rubicons cloud-upload" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke="currentColor" fill="none">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 20V10"></path>
                        <path stroke-linecap="round" d="M16 17a4.9997 4.9997 0 005-5 5 5 0 00-5-5 4.9362 4.9362 0 00-1.088.127 4.9874 4.9874 0 00-2.1548-3.3522 4.9875 4.9875 0 00-5.7648.1604A4.988 4.988 0 005.232 9.427 3.989 3.989 0 007 17h1"></path>
                        <path stroke-linecap="round" d="M9 13l3-3 3 3"></path>
                    </svg>
                </div>
                <div className="text-text font-roboto font-medium text-2xl">
                    Drag and drop or choose a file
                </div>
            </label>
            <input type="file" id="file" name="files" accept=".png,.jpg,.webp" className="hidden" />
        </div>
    )
}