import Hero from '@/components/Hero'
import Services from '@/components/Services'
import Contact from '@/components/Contact'
import Navbar from '@/components/Navbar'
import Footer from '@/components/Footer'

export default function Home() {
  return (
    <main>
      <Navbar />
      <Hero />
      <Services />
      <Contact />
      <Footer />
    </main>
  )
}
