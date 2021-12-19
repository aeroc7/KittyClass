import Logo from "../components/Logo"
import Head from "next/head"
import DragDrop from "../components/DragDrop"
import { useState } from 'react';

export default function Index() {
    const [resulting_data, setData] = useState("Upload an image of a cat or dog");

    const updateContent = (data) => {
        var type = data.split(',')[0];
        var conf = data.split(',')[1];
        var fmtd_data = `Predicted image is a ${type} with ${conf}% confidence.`;

        setData(fmtd_data);
    };

    return (
        <>
            <div className="relative h-screen w-screen">
                <Head>
                    <title>KittyClass</title>
                    <meta name="description" content="Classify your dog or cat using a neural network." />
                </Head>
                <div>
                    <Logo />
                    <div className="pt-20">
                        <DragDrop onResponse={updateContent} />
                    </div>
                    <div className="flex justify-center pt-7">
                        <div className="block text-white text-center font-roboto max-w-xs sm:max-w-full">{`${resulting_data}`}</div>
                    </div>
                </div>
            </div>
        </>
    )
}
