'use client'

import Link from 'next/link'
import { useState } from 'react'

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <nav className="bg-white shadow-lg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex items-center">
            <Link href="/" className="text-2xl font-bold text-primary-600">
              CRSET Solutions
            </Link>
          </div>
          
          <div className="hidden md:flex items-center space-x-8">
            <Link href="#services" className="text-gray-700 hover:text-primary-600 transition-colors">
              Serviços
            </Link>
            <Link href="#contact" className="text-gray-700 hover:text-primary-600 transition-colors">
              Contacto
            </Link>
            <Link href="/dashboard" className="btn-primary">
              Dashboard
            </Link>
          </div>

          <div className="md:hidden flex items-center">
            <button
              onClick={() => setIsOpen(!isOpen)}
              className="text-gray-700 hover:text-primary-600"
            >
              <svg className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
              </svg>
            </button>
          </div>
        </div>
      </div>

      {isOpen && (
        <div className="md:hidden">
          <div className="px-2 pt-2 pb-3 space-y-1 sm:px-3 bg-white border-t">
            <Link href="#services" className="block px-3 py-2 text-gray-700 hover:text-primary-600">
              Serviços
            </Link>
            <Link href="#contact" className="block px-3 py-2 text-gray-700 hover:text-primary-600">
              Contacto
            </Link>
            <Link href="/dashboard" className="block px-3 py-2 text-primary-600 font-medium">
              Dashboard
            </Link>
          </div>
        </div>
      )}
    </nav>
  )
}
