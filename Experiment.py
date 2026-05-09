
from ModelUsageData import ModelUsageData, write_usage_to_csv



from ResponseQuality import  ResponseQuality
from AnthropicChatTest import AnthropicChatTest



questions = [
    # 1. Audio — codec comparison
    "I listen to lossless music on my phone. Compare LDAC, aptX HD, and LC3 Bluetooth codecs "
    "and tell me which over-ear headphones under $300 would give me the best audio quality.",

    # 2. Storage — NVMe upgrade trade-off
    "My video editing workstation currently has a SATA SSD. Would upgrading to an NVMe PCIe Gen 4 "
    "drive noticeably speed up my workflow, and what TBW rating should I look for?",

    # 3. Computing — laptop vs tablet for students
    "I am a university student studying data science. Should I buy a high-end tablet with a "
    "keyboard or a mid-range laptop? Compare them on performance, portability, and software support.",

    # 4. Smartphone — structured evaluation framework
    "Walk me through a structured framework for choosing a flagship smartphone in 2025, covering "
    "SoC benchmarks, camera sensor specs, 5G band support, and software update commitments.",

    # 5. Ergonomics — office chair for back pain
    "I work from home for 10 hours a day and have lower-back pain. What ergonomic chair features "
    "should I prioritise — lumbar support, seat depth, armrest adjustability — and what price tier "
    "offers genuine ergonomic benefit versus marketing?",

    # 6. Recommendation systems — deep learning models
    "Explain how a two-tower deep learning recommendation model works on an e-commerce platform, "
    "and describe how implicit signals like dwell time differ from explicit signals like star ratings.",

    # 7. Platform trust — counterfeits and dynamic pricing
    "How do major online marketplaces detect counterfeit products and protect buyers? Also explain "
    "how dynamic pricing works and how a shopper can tell if a 'sale' price is genuine.",

    # 8. Cloud — AWS vs Azure vs GCP for SMBs
    "A small business with 20 employees is moving from on-premise servers to the cloud. "
    "Compare AWS, Azure, and Google Cloud on pricing model, ease of migration, and SMB support, "
    "and outline the key TCO factors they should calculate before committing.",

    # 9. Purchasing framework — home office budget allocation
    "I have a $1,500 budget for a home office setup covering a monitor, mechanical keyboard, and "
    "webcam. Apply a needs-assessment and budget-tiering framework to recommend the best allocation "
    "across those three categories.",

    # 10. Logistics — cross-border shopping risks
    "What should I know about customs duties, delivery timelines, and return policies when buying "
    "consumer electronics from an overseas marketplace? How do I evaluate whether the price saving "
    "is worth the added risk?",

    # 11. Audio — in-ear monitors for gym use
    "I want in-ear headphones for gym workouts — they must stay in place, be sweat-resistant, "
    "and have at least 8 hours of battery. What specs matter most and which models are worth "
    "considering under $150?",

    # 12. Storage — NAS vs cloud backup for home users
    "Should I build a home NAS using 3.5-inch HDDs or subscribe to a cloud backup service "
    "for storing 20TB of photos and videos? Compare cost over 5 years, reliability, and "
    "access speed.",

    # 13. Computing — gaming laptop thermal and GPU trade-offs
    "I want a gaming laptop that can also handle 3D rendering. How do I evaluate thermal "
    "management, GPU TDP limits, and display refresh rate to avoid paying for specs I cannot "
    "actually sustain under load?",

    # 14. Peripherals — mechanical keyboard switch selection
    "I type for 8 hours a day and occasionally game in the evenings. Walk me through the "
    "differences between linear, tactile, and clicky mechanical switches and recommend "
    "specific switch types for my use case.",

    # 15. E-commerce — last-mile delivery and fulfilment models
    "Explain the difference between marketplace fulfilment programmes like FBA and a seller "
    "shipping independently. How does each model affect delivery speed, return experience, "
    "and product listing visibility?",

    # 16. Pricing strategy — subscription discounts and cashback
    "Online retailers offer subscribe-and-save discounts, store credit cards, and cashback "
    "portals. How should I stack these to maximise savings without overspending, and what "
    "pitfalls should I watch out for?",

    # 17. Cloud — IaaS vs PaaS vs SaaS decision guide
    "My startup needs to deploy a web application with a PostgreSQL database and a machine "
    "learning inference endpoint. Should I use IaaS, PaaS, or a mix of both? Walk me through "
    "the decision with cost and operational complexity in mind.",

    # 18. Smartphone — camera sensor deep-dive
    "Explain the real-world impact of sensor size, aperture, and optical image stabilisation "
    "on smartphone photography. How do I compare two phones where one has a larger sensor "
    "but a narrower aperture than the other?",

    # 19. Purchasing framework — future-proofing a monitor purchase
    "I am buying a monitor for graphic design and occasional gaming. How do I future-proof "
    "the purchase by evaluating panel type, colour gamut coverage, adaptive sync standard, "
    "and port selection over a 5-year horizon?",

    # 20. Trust and safety — evaluating a new online seller
    "I found a significantly cheaper price for a high-value electronics item from an unfamiliar "
    "online seller. What signals — seller rating, listing quality, payment protection, return "
    "policy — should I check to decide whether the deal is trustworthy?",
]
 

qc = ResponseQuality()



def RunAnthropicTest(): 
    
    anthChat = AnthropicChatTest()
    
    miData: list[ModelUsageData]= [] 
    miData = anthChat.perform_cost_time(questions)
    
    

    write_usage_to_csv("Anthropic_result.csv",miData )
    
    print('Generated result for Anthropic')


RunAnthropicTest()
