import Logo from "../components/Logo"
import Head from "next/head"
import DragDrop from "../components/DragDrop"

export default function Index() {
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
                        <DragDrop />
                    </div>
                </div>

            </div>
        </>
    )
}
